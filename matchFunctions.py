#!/user/bin/env python

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
import os, sys, random
from classes import cardbase, gamebase, playerbase
import tcgpowers, mechanics, config
import json

#For cogs when needed
mechanics.initData()
startup_extensions = ['cogs.infocommands','cogs.deckbuilding','cogs.collecting']
matches = {}

#Bot setup
TOKEN = config.TOKEN
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
	
#Send hand function
@asyncio.coroutine
def sendHand( player, playerObj, ctx ):
	#delete last hand sent
	if not playerObj.lastHandDM == None:
		yield from bot.delete_message( playerObj.lastHandDM )
	
	#send hand
	stringSend = ""
	for cards in playerObj.hand:
		stringSend += str( mechanics.cardList[cards.lower()] ) + "\n"
	playerObj.lastHandDM = yield from bot.send_message( player, "[-----Hand-----]\n" + stringSend + "\n\n" )
	
#Active player played a card
@asyncio.coroutine
def playCard( match, activePlayer, activePlayerObj, opponent, opponentObj, cardName, targets, ctx ):

	playedObject = mechanics.cardList[cardName.lower()]
	
	#Pay health if possible
	if activePlayerObj.lifeforce <= playedObject.cost:
		yield from bot.send_message( ctx.message.channel, "You don't have enough lifeforce for that card." )
		return
	else:
		activePlayerObj.lifeforce -= playedObject.cost
		
	#Remove card from hand
	for card in activePlayerObj.hand:
		if card.lower() == cardName:
			activePlayerObj.hand.remove( card )
			break
		
	#Play the card (assuming already got proper targets)
	playedObject.func( activePlayerObj, opponentObj, targets )
	yield from bot.send_message( ctx.message.channel, activePlayer.name + " played " + str(playedObject) + "\n\n" )
	
	#Check for lethal damage
	if opponentObj.lifeforce <= 0:
		yield from mechanics.gameOver( activePlayer, opponent, matches, bot, ctx )
		return False
	elif activePlayerObj.lifeforce <= 0:
		yield from mechanics.gameOver( opponent, activePlayer, matches, bot, ctx )
		return False
			
	#Send hand & messages
	activePlayerObj.cardsThisTurn += 1
	yield from sendHand( activePlayer, activePlayerObj, ctx )
	if not match.gameMessage == None:
		yield from bot.delete_message( match.gameMessage )
	match.gameMessage = yield from bot.send_message( ctx.message.channel, str(activePlayerObj)+"\n\n"+str(opponentObj)+"\nCommands: play, concede, pass, info, mill" )
	return True
	
@asyncio.coroutine
def getTarget( playedObject, activePlayerObj, activePlayer, otherPlayerObj, ctx ):
	targetEmojis = ['0⃣','1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣','9⃣', '🔟']
	if playedObject.targets == None:
		return None
	elif playedObject.targets == "ENEMY_NODE":
		#React to self up to amount of enemy nodes (if none, then continue big loop)
		if len(otherPlayerObj.nodes) == 0:
			yield from bot.send_message( ctx.message.channel, "No nodes to target." )
			return False #if False, continue
			
		msg = yield from bot.send_message( ctx.message.channel, "Use reactions to indicate which of your opponent's Nodes to target." )
		for i in range( len(otherPlayerObj.nodes) ):
			yield from bot.add_reaction( msg, targetEmojis[i+1] )
			
		#Wait for reaction from that list
		res = yield from bot.wait_for_reaction( emoji=targetEmojis, message=msg, user=activePlayer )
		thisTarget = targetEmojis.index(str(res.reaction.emoji))-1
		return thisTarget
	elif playedObject.targets == "FRIENDLY_NODE":
		#React to self up to amount of friendly nodes (if none, then continue big loop)
		if len(activePlayerObj.nodes) == 0:
			yield from bot.send_message( ctx.message.channel, "No nodes to target." )
			return False
			
		msg = yield from bot.send_message( ctx.message.channel, "Use reactions to indicate which of your Nodes to target." )
		for i in range( len(activePlayerObj.nodes) ):
			yield from bot.add_reaction( msg, targetEmojis[i+1] )
			
		#Wait for reaction from that list
		res = yield from bot.wait_for_reaction( emoji=targetEmojis, message=msg, user=activePlayer )
		thisTarget = targetEmojis.index(str(res.reaction.emoji))-1
		return thisTarget
		
	elif playedObject.targets == "PLAYER":
		msg = yield from bot.send_message( ctx.message.channel, "Use reactions to indicate which player to target (1 is yourself, 2 is your opponent)." )
		for i in range( 2 ):
			yield from bot.add_reaction( msg, targetEmojis[i+1] )
		res = yield from bot.wait_for_reaction( emoji=targetEmojis, message=msg, user=activePlayer )
		thisTarget = targetEmojis.index(str(res.reaction.emoji))-1
		return thisTarget
		
#New round in a match started
@asyncio.coroutine
def startRound( match, activePlayer, activePlayerObj, otherPlayer, otherPlayerObj, ctx ):

	#check if milled out when drawing a card (maybe condense this chunk somehow)
	if not activePlayerObj.drawCard():
		yield from bot.send_message( ctx.message.channel, activePlayer.name + " milled out!" )
		yield from mechanics.gameOver( otherPlayer, activePlayer, matches, bot, ctx )
		return
	
	#Energy costs (oooh actual phase orders are showing c:)
	activePlayerObj.lifeforce += activePlayerObj.energy
	
	#Activate all of active player's nodes/initialize turn-based vars
	for thisNode in activePlayerObj.nodes:
		mechanics.activateNode( thisNode, activePlayerObj, otherPlayerObj, activePlayer, otherPlayer, matches, bot )
		yield from bot.send_message( ctx.message.channel, activePlayerObj.name + " activated Node: " + str(mechanics.nodeList[thisNode.lower()]) )
	activePlayerObj.newTurn()
	otherPlayerObj.newTurn()
	activePlayerObj.newMyTurn()
	
	#check if dead
	if otherPlayerObj.lifeforce <= 0:
		yield from mechanics.gameOver( activePlayer, otherPlayer, matches, bot, ctx )
		return
	elif activePlayerObj.lifeforce <= 0:
		yield from mechanics.gameOver( otherPlayer, activePlayer, matches, bot, ctx )
		return
		
	#Send the info
	yield from bot.send_message( ctx.message.channel, activePlayer.name + "'s turn." )
	if not match.gameMessage == None:
		yield from bot.delete_message( match.gameMessage )
	match.gameMessage = yield from bot.send_message( ctx.message.channel, str(activePlayerObj)+"\n\n"+str(otherPlayerObj)+"\nCommands: play, concede, pass, info, mill" )
	
	yield from sendHand( activePlayer, activePlayerObj, ctx )
	
	#Make sure it's a game command
	def check(msg):
		return msg.content.lower().startswith('play') or msg.content.lower().startswith('concede') or msg.content.lower().startswith('pass') or msg.content.lower().startswith('info') or msg.content.lower().startswith('mill')
	
	#Wait for active player's command.
	while True:
		messageOriginal = yield from bot.wait_for_message( author=activePlayer, check=check, timeout=config.TURN_TIMEOUT )
		
		#Act within 500 seconds or game is lost
		try:
			message = messageOriginal.content.lower().split(' ',1)
		except AttributeError:
			yield from bot.send_message( ctx.message.channel, "Game timed out!" )
			yield from mechanics.gameOver( otherPlayer, activePlayer, matches, bot, ctx )
			break
	
		if message[0] == 'info':
			if not match.gameMessage == None:
				yield from bot.delete_message( match.gameMessage )
			match.gameMessage = yield from bot.send_message( ctx.message.channel, str(activePlayerObj)+"\n\n"+str(otherPlayerObj)+"\nCommands: play, concede, pass, info, mill" )
			continue
		elif message[0] == 'play': #The big one
			
			#Ensure it's in hand
			if not any(message[1] in x.lower() for x in activePlayerObj.hand):
				yield from bot.send_message( ctx.message.channel, "Played an invalid card." )
				continue
				
			#Get proper targets
			playedObject = mechanics.cardList[message[1].lower()]
			thisTarget = yield from getTarget( playedObject, activePlayerObj, activePlayer, otherPlayerObj, ctx )
			if thisTarget == False:
				continue
			
			#Check if node generator (for 1 per turn limit)
			if playedObject.cardtype == "NodeGen":
				if activePlayerObj.playedNode:
					yield from bot.send_message( ctx.message.channel, "You already spawned a Node this turn." )
					continue
				else:
					activePlayerObj.playedNode = True
			keepGoing = yield from playCard( match, activePlayer, activePlayerObj, otherPlayer, otherPlayerObj, message[1], thisTarget, ctx )
			if not keepGoing:
				print('did this')
				return
				
			continue
			
		elif message[0] == 'pass':
			yield from startRound( match, otherPlayer, otherPlayerObj, activePlayer, activePlayerObj, ctx )
			break
		elif message[0] == 'mill':
			if activePlayerObj.milled == True:
				yield from bot.send_message( ctx.message.channel, "You already milled a card this turn." )
				continue
			elif len(activePlayerObj.deck) <= 0:
				yield from bot.send_message( ctx.message.channel, "You have no cards to mill." )
				continue
			else:
				activePlayerObj.milled = True
				poppedCard, lifeToGain = mechanics.millCard( activePlayerObj )
				yield from bot.send_message( ctx.message.channel, activePlayerObj.name + " milled " + poppedCard + " for " + str(lifeToGain) + " health." )
				continue
		elif message[0] == 'concede':
			yield from bot.send_message( ctx.message.channel, activePlayer.name + " conceded." )
			yield from mechanics.gameOver( otherPlayer, activePlayer, matches, bot, ctx )
			return

#Challenge someone and initialize the fight
@bot.command(pass_context=True)
@asyncio.coroutine
def challenge( ctx, target: discord.Member = None, *args ):
	"""Challenge a friend to discordTCG! =challenge <@user> <wager>"""
	
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
	message = yield from bot.wait_for_message( author=target, content='accept', timeout=config.CHALLENGE_TIMEOUT )
	if message is None:
		yield from bot.say( challenger + ", your challenge was not accepted :(" )
		return
	
	#check again here for duplicate accepts
	if challenger in matches or target.name in matches:
		yield from bot.say( "A player is already in a match." )
		return
	
	#Get player data
	challengerDeck = mechanics.getPlyData( ctx.message.author )
	defenderDeck = mechanics.getPlyData( target )
	if defenderDeck is None or challengerDeck is None:
		yield from bot.say( "Both players aren't registered! Use =register." )
		return
	challengerDeck = challengerDeck['decks'][challengerDeck['selectedDeck']]
	defenderDeck = defenderDeck['decks'][defenderDeck['selectedDeck']]
	if len(challengerDeck) < config.DECK_SIZE_MINIMUM or len(defenderDeck) < config.DECK_SIZE_MINIMUM:
		yield from bot.say( "A player doesn't have at least "+str(config.DECK_SIZE_MINIMUM)+" cards in his or her deck." )
		return
		
	#Wager stuff
	try:
		wager = int(args[0])
		if mechanics.getBal( ctx.message.author.id ) < wager or mechanics.getBal( target.id ) < wager:
			yield from bot.say( "A player doesn't have enough money for this wager!" )
			return
		yield from bot.say( "Wager set to $" + args[0] + "!" )
	except:
		wager = 0
	
	#Initialize game
	matches[challenger] = gamebase.TCGame( challenger, target.name, wager )
	matches[challenger].chalObj = playerbase.Player( challenger, challengerDeck, [] )
	matches[challenger].defObj = playerbase.Player( target.name, defenderDeck, [] )
	matches[challenger].chalObj.shuffle()
	matches[challenger].defObj.shuffle()
	for i in range(config.STARTING_HAND_SIZE):
		matches[challenger].chalObj.drawCard()
		matches[challenger].defObj.drawCard()
	matches[challenger].chalObj.opponent = matches[challenger].defObj
	matches[challenger].defObj.opponent = matches[challenger].chalObj
	print('A match has started. ' + str(challenger) + ' vs ' + str(target.name) + '!')
	
	#Start round 
	if random.randint(0,1) == 0:
		matches[challenger].chalObj.active = True
		matches[challenger].defObj.energy += 1
		yield from startRound( matches[challenger], ctx.message.author, matches[challenger].chalObj, target, matches[challenger].defObj, ctx )
	else:
		matches[challenger].defObj.active = True
		matches[challenger].chalObj.energy += 1
		yield from startRound( matches[challenger], target, matches[challenger].defObj, ctx.message.author, matches[challenger].chalObj, ctx )

print("[-=-Loaded Cards-=-]\n")
for cards in mechanics.cardList:
	print(cards)
print("\n[-=-Loaded Nodes-=-]\n")
for nodes in mechanics.nodeList:
	print(nodes)

bot.run( TOKEN )
