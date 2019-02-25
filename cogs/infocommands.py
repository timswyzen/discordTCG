#!/user/bin/env python
import discord
from discord.ext import commands
import asyncio, json, os
from mechanics import cardList, nodeList, getPlyData
import config

"""Extra commands that didn't need to be in the base file"""

defaultDeck1 = ["Minor Recharge", "Minor Recharge", "Killer's Aura", "Killer's Aura", "Snipe", "Snipe", "Hivemind", "Hivemind", "Hivemind", "Swing", "Swing", "Swing", "Minor Panic", "Minor Panic", "Minor Panic", "Swarmspark", "Swarmspark", "Swarmspark", "Inherited Cruelty", "Inherited Cruelty", "Inherited Cruelty", "Recursion", "Recursion", "Recursion", "Gluttonous Temptation", "Neuron Boost", "Neuron Boost", "Siphon Power", "Siphon Power", "Siphon Power", "Stimulation", "Stimulation", "Maul", "Backlash", "Collected Shot", "Double Tap", "Beg for Mercy", "Beg for Mercy", "Creativity", "Creativity"]

defaultDeck2 = ["Maul", "Snipe", "Snipe", "Swing", "Swing", "Swing", "Stimulation", "Stimulation", "Double Tap", "Minor Recharge", "Minor Recharge", "Neuron Boost", "Neuron Boost", "Minor Panic", "Minor Panic", "Minor Panic", "Beg for Mercy", "Beg for Mercy", "Fizzle", "Fizzle", "False Hope", "False Hope", "Shattered Mind", "Last Meal", "Last Meal", "Last Crumb", "Last Crumb", "Recursion", "Recursion", "Voracity", "Voracity", "Mind Swap", "Mind Swap", "Voracity", "Unwilling Sacrifice", "Unwilling Sacrifice", "Bloody Pentagram", "Bloody Pentagram", "Siphon Power", "Siphon Power", "Confusion", "Confusion"]

class InfoCommands():
	def __init__(self, bot):
		self.bot = bot
		
	#Search via description
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def search( self, ctx, *args ):
		"""Search for a card via its description."""
		queryList = args
		stringToSay = ""
		i = 0
		for card in cardList:
			sayCard = True
			for query in queryList:
				if query.lower() not in cardList[card].desc.lower() and query.lower() not in cardList[card].name.lower():
					sayCard = False
			if sayCard == True:
				stringToSay += str(cardList[card]) + '\n'
				i+=1
				if i>=10:
					i=0
					yield from self.bot.say( stringToSay )
					stringToSay = ""
		if not stringToSay == "":
			yield from self.bot.say( stringToSay )
		
	#Get Node information 
	@commands.command(pass_context=True)	
	@asyncio.coroutine
	def node( self, ctx, *args ):
		"""Query the bot for information on a Node."""
		try:
			query = ' '.join( args ).lower()
			if query.lower() in nodeList:
				yield from self.bot.say( str( nodeList[query.lower()] ) )
			else:
				yield from self.bot.say( "Node not found." )
		except Exception as e:
			print(e)
			
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def library( self, ctx, *args ):
		"""See how many cards there are in the game."""
		commons, uncommons, rares = [], [], []
		for card in cardList:
			if cardList[card].rarity == 'C':
				commons.append( cardList[card].name )
			elif cardList[card].rarity == 'U':
				uncommons.append( cardList[card].name )
			elif cardList[card].rarity == 'R':
				rares.append( cardList[card].name )
		yield from self.bot.say( str(len(commons)) + " Commons, " + str(len(uncommons)) + " Uncommons, and " + str(len(rares)) + " Rare cards exist.\nThere are " + str(len(commons)+len(uncommons)+len(rares)) + " cards in total, not counting Special cards." )
	
	#Get card information 
	@commands.command(pass_context=True)	
	@asyncio.coroutine
	def card( self, ctx, *args ):
		"""Query the bot for information on a card."""
		try:
			query = ' '.join( args ).lower()
			if query in cardList:
				yield from self.bot.say( str( cardList[query.lower()] ) )
			else:
				yield from self.bot.say( "Card not found." )
		except Exception as e:
			print(e)
			
	#Get game definition
	@commands.command(pass_context=True)	
	@asyncio.coroutine
	def define( self, ctx, *args ):
		"""Query the bot for the definition of a game term."""
		try:
			query = ' '.join( args )
			if query in config.DEFINITIONS.keys():
				yield from self.bot.say( config.DEFINITIONS[query.lower()] )
			else:
				yield from self.bot.say( "Term not found." )
		except Exception as e:
			print(e)
			
	#Show off a card
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def showoff( self, ctx, *args  ):
		"""Show off a card. And don't try to lie!"""
		try:
			card = ' '.join( args )
			cardLower = card.lower()
		except:
			yield from self.bot.say( "Incorrect syntax. =showoff <cardname>" )
		
		if cardLower in [x.lower() for x in getPlyData( ctx.message.author )['collection'].keys()]:
			yield from self.bot.say( ctx.message.author.name + " has a shiny " + card + "!" )
		else:
			yield from self.bot.say( ctx.message.author.name + " doesn't even have a " + card + ". What a loser!" )
			
	#Credits
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def credits( self, ctx, *args ):
		"""See who worked in this kick-butt project!"""
		yield from self.bot.say( "[-------------=Credits=-------------]\n---[--------Version "+config.VERSION+"--------]---\n**Developer/Creator**: Tim Swyzen\n**Game Design**: John Kay, Tim Swyzen" )
		
	#Tutorial
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def tutorial( self, ctx, *args ):
		"""Get a link to the beginner's guide."""
		yield from self.bot.say( "Beginner's Guide: https://pastebin.com/Y70FZ49Q" )
			
	#Get an 'account'
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def register( self, ctx ):
		"""Get an account before you can start playing"""
		playerID = ctx.message.author.id
		if os.path.isfile('player_data/'+str(playerID)+'.txt'):
			yield from self.bot.say( "You're already registered." )
			return
		playerData = {
			"collection": {
				"Maul": 1,
				"Killer's Aura": 2,
				"Snipe": 2,
				"Gluttonous Temptation": 1,
				"Hivemind": 3,
				"Swing": 3,
				"Minor Panic": 3,
				"Swarmspark": 3,
				"Stimulation": 2,
				"Inherited Cruelty": 3,
				"Recursion": 2,
				"Double Tap": 1,
				"Neuron Boost": 2,
				"Siphon Power": 3,
				"Backlash": 1,
				"Creativity": 2,
				"Minor Recharge": 2,
				"Beg For Mercy": 2,
				"Collected Shot": 1,
				"Confusion": 2,
				"Mind Swap": 2,
				"Fizzle": 2,
				"Voracity": 3,
				"Unwilling Sacrifice": 2,
				"False Hope": 2,
				"Shattered Mind": 1,
				"Last Meal": 2,
				"Last Crumb": 2,
				"Bloody Pentagram": 2
			},
			"selectedDeck": 0,
			"money": 50,
			"packs": 4,
			"decks": [ defaultDeck1, defaultDeck2, [], [], [] ],
			"decknames": [ "Swarmers", "H/D Combo", "", "", "" ] #just cleaner than making "decks" a dic116540929418067968t...
		}
		
		#give testers 4 of each card
		testers = ['135526460881502209','128216983605870603',]
		if ctx.message.author.id in testers:
			playerData['collection'] = {}
			for files in os.listdir('./cards'):
				playerData['collection'][files[:-3]] = 4
		
		with open('player_data/'+str(playerID)+'.txt', 'w') as outfile:
			json.dump(playerData, outfile)
		
		yield from self.bot.say( "Registration successful!" )

		
def setup(bot):
	bot.add_cog(InfoCommands(bot))
