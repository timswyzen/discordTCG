#!/user/bin/env python

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
import os, sys, random
from classes import cardbase, gamebase, playerbase
import tcgpowers, mechanics
import json

#For cogs when needed
mechanics.initData()
startup_extensions = ['cogs.infocommands']
matches = {}

#Bot setup
TOKEN = 'NTQ1NzAxMDgwMDQ3MDI2MTc2.D0dfTQ.V_xdcXWNcoIhZ_XdP6G1EtlWNJs'
bot = commands.Bot( command_prefix = '=' )

#Load extensions
@bot.event
@asyncio.coroutine
def on_ready():
	for extension in startup_extensions:
		try:
			bot.load_extension( extension )
			print( "Successfully loaded " + str(extension) + "!" )
		except Exception as e:
			print( "Extension load failed: " + str(extension) + ".\nMessage: " + str(e) )
	
#Active player played a card
@asyncio.coroutine
def playCard( match, activePlayer, activePlayerObj, opponent, opponentObj, cardName, targets, ctx ):

	playedObject = mechanics.cardList[cardName.lower()]
	
	#Pay health if possible
	if activePlayerObj.lifeforce <= playedObject.cost:
		yield from bot.send_message( ctx.message.channel, "You don't have enough lifeforce for that card." )
		return
	else:
		activePlayerObj.lifeforce = activePlayerObj.lifeforce - playedObject.cost
		
	#Play the card (assuming already got proper targets)
	playedObject.func( activePlayerObj, opponentObj, targets )
	yield from bot.send_message( ctx.message.channel, activePlayer.name + " played " + str(playedObject) + "\n\n" )
	
	#Check for lethal damage
	if opponentObj.lifeforce <= 0:
		mechanics.gameOver( activePlayerObj, opponentObj, matches )
	elif activePlayerObj.lifeforce <= 0:
		mechanics.gameOver( opponentObj, activePlayerObj, matches )
	
	#Remove card from hand
	for card in activePlayerObj.hand:
		if card.lower() == cardName:
			activePlayerObj.hand.remove( card )
			break
			
	yield from bot.send_message( ctx.message.channel, str(activePlayerObj)+"\n\n"+str(opponentObj) )
		
#New round in a match started
@asyncio.coroutine
def startRound( match, activePlayer, activePlayerObj, otherPlayer, otherPlayerObj, ctx ):

	#check if milled out when drawing a card (maybe condense this chunk somehow)
	if not activePlayerObj.drawCard():
		yield from bot.send_message( ctx.message.channel, activePlayer.name + " milled out!" )
		mechanics.gameOver( otherPlayer, activePlayer, matches )
		yield from bot.send_message( ctx.message.channel, activePlayer.name + " just lost to " + otherPlayer.name + " in discordTCG!" )
		return
	
	#Energy costs (oooh actual phase orders are showing c:)
	activePlayerObj.lifeforce = activePlayerObj.lifeforce + activePlayerObj.energy
	
	#Activate all of active player's nodes/initialize turn-based vars
	for thisNode in activePlayerObj.nodes:
		mechanics.activateNode( thisNode, activePlayerObj, otherPlayerObj, matches )
		yield from bot.send_message( ctx.message.channel, activePlayerObj.name + " activated Node: " + thisNode )
	activePlayerObj.newTurn()
	otherPlayerObj.newTurn()
	activePlayerObj.active = True
		
	#Send the info
	yield from bot.send_message( ctx.message.channel, activePlayer.name + "'s turn." )
	yield from bot.send_message( ctx.message.channel, str(activePlayerObj)+"\n\n"+str(otherPlayerObj) )
	yield from bot.send_message( activePlayer, "Hand: " + str(activePlayerObj.hand) )
	yield from bot.send_message( otherPlayer, "Hand: " + str(otherPlayerObj.hand) )
	
	#Make sure it's a game command
	def check(msg):
		return msg.content.lower().startswith('play') or msg.content.lower().startswith('concede') or msg.content.lower().startswith('pass') or msg.content.lower().startswith('info') or msg.content.lower().startswith('mill')
	
	#Wait for active player's command.
	while True:
		yield from bot.send_message( ctx.message.channel, "Commands: play, concede, pass, info, mill" )
		message = yield from bot.wait_for_message( author=activePlayer, check=check, timeout=500 )
		
		#Act within 500 seconds or game is lost
		try:
			message = message.content.lower().split(' ',1)
		except AttributeError:
			yield from bot.send_message( ctx.message.channel, "Game timed out!" )
			mechanics.gameOver( otherPlayer, activePlayer, matches )
			yield from bot.send_message( ctx.message.channel, activePlayer.name + " just lost to " + otherPlayer.name + " in discordTCG!" )
			break
	
		if message[0] == 'info':
			yield from bot.send_message( ctx.message.channel, str(activePlayerObj)+"\n\n"+str(otherPlayerObj) )
			continue
		elif message[0] == 'play': #The big one
			
			#Ensure it's in hand
			if not any(message[1] in x.lower() for x in activePlayerObj.hand):
				yield from bot.send_message( ctx.message.channel, "Played an invalid card." )
				continue
				
			#Get proper targets
			playedObject = mechanics.cardList[message[1].lower()]
			targetEmojis = ['0⃣','1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣','9⃣', '🔟']
			if playedObject.targets == None:
				yield from playCard( match, activePlayer, activePlayerObj, otherPlayer, otherPlayerObj, message[1], None, ctx )
			elif playedObject.targets == "ENEMY_NODE":
				#React to self up to amount of enemy nodes (if none, then continue big loop)
				if len(otherPlayerObj.nodes) == 0:
					yield from bot.send_message( ctx.message.channel, "No nodes to target." )
					continue
					
				msg = yield from bot.send_message( ctx.message.channel, "Use reactions to indicate which of your opponent's Nodes to target." )
				for i in range( len(otherPlayerObj.nodes) ):
					yield from bot.add_reaction( msg, targetEmojis[i+1] )
					
				#Wait for reaction from that list
				res = yield from bot.wait_for_reaction( emoji=targetEmojis, message=msg, user=activePlayer )
				thisTarget = targetEmojis.index(str(res.reaction.emoji))-1
				yield from playCard( match, activePlayer, activePlayerObj, otherPlayer, otherPlayerObj, message[1], thisTarget, ctx )
				
			continue
			
		elif message[0] == 'pass':
			yield from startRound( match, otherPlayer, otherPlayerObj, activePlayer, activePlayerObj, ctx )
			break
		elif message[0] == 'mill':
			if activePlayerObj.milled == True:
				yield from bot.send_message( ctx.message.channel, "You already milled a card this turn." )
				continue
			else:
				activePlayerObj.milled = True
				mechanics.millCard( activePlayerObj )
				yield from bot.send_message( ctx.message.channel, ply.name + " milled " + poppedCard + " for " + str(lifeToGain) + " health." )
				continue
		elif message[0] == 'concede':
			yield from bot.send_message( ctx.message.channel, activePlayer.name + " conceded." )
			mechanics.gameOver( otherPlayer, activePlayer, matches )
			yield from bot.send_message( ctx.message.channel, activePlayer.name + " just lost to " + otherPlayer.name + " in discordTCG!" )
			break

#Challenge someone and initialize the fight
@bot.command(pass_context=True)
@asyncio.coroutine
def challenge( ctx, target: discord.Member = None ):
	"""Challenge a friend to discordTCG!"""
	
	challenger = ctx.message.author.name
	
	#Make sure neither player is in a game currently
	if challenger in matches or target.name in matches:
		yield from bot.say( "A player is already in a match." )
		return
		
	#Dont challenge yourself man
	if ctx.message.author == target:
		yield from bot.say( "You can't challenge yourself, silly!" )
		return
	
	#Have challenged guy accept
	yield from bot.say( target.name + ", you've been challenged to a discordTCG match! Type 'accept' to accept." )
	message = yield from bot.wait_for_message( author=target, content='accept', timeout=20 )
	if message is None:
		yield from bot.say( challenger + ", your challenge was not accepted :(" )
		return
	
	#Get player data
	challengerDeck = mechanics.getPlyData( ctx.message.author )
	defenderDeck = mechanics.getPlyData( target )
	challengerDeck = challengerDeck['selectedDeck']
	defenderDeck = defenderDeck['selectedDeck']
	if defenderDeck is None or challengerDeck is None:
		yield from bot.say( "Both players aren't registered! Use =register." )
		return
	
	#Initialize game
	matches[challenger] = gamebase.TCGame( challenger, target.name )
	matches[challenger].chalObj = playerbase.Player( challenger, challengerDeck, ['Get Puncher','Snipe'] )
	matches[challenger].defObj = playerbase.Player( target.name, defenderDeck, ['Get Puncher','Embrace Temptation'] )
	matches[challenger].chalObj.shuffle()
	matches[challenger].defObj.shuffle()
	
	#Start round 
	if random.randint(0,1) == 0:
		matches[challenger].chalObj.active = True #deprecated? TODO: see if I actually need this
		yield from startRound( matches[challenger], ctx.message.author, matches[challenger].chalObj, target, matches[challenger].defObj, ctx )
	else:
		matches[challenger].defObj.active = True
		yield from startRound( matches[challenger], target, matches[challenger].defObj, ctx.message.author, matches[challenger].chalObj, ctx )

print("[-=-Loaded Cards-=-]\n")
for cards in mechanics.cardList:
	print(cards)
print("\n[-=-Loaded Nodes-=-]\n")
for nodes in mechanics.nodeList:
	print(nodes)

bot.run( TOKEN )
