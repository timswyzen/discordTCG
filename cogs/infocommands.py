#!/user/bin/env python
import discord
from discord.ext import commands
import asyncio, json, os
from mechanics import cardList, nodeList, getPlyData
import config

"""Extra commands that didn't need to be in the base file"""

class InfoCommands():
	def __init__(self, bot):
		self.bot = bot
		
	#Get Node information 
	@commands.command(pass_context=True)	
	@asyncio.coroutine
	def node( self, ctx, *args ):
		"""Query the bot for information on a Node."""
		try:
			query = ' '.join( args )
			if query.lower() in nodeList:
				yield from self.bot.say( str( nodeList[query.lower()] ) )
			else:
				yield from self.bot.say( "Card not found." )
		except Exception as e:
			print(e)
	
	#Get card information 
	@commands.command(pass_context=True)	
	@asyncio.coroutine
	def card( self, ctx, *args ):
		"""Query the bot for information on a card."""
		try:
			query = ' '.join( args )
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
				"Swing": 4,
				"Get Puncher": 3,
				"Recursion": 2,
				"Voracity": 2,
				"Minor Panic": 2,
				"Embrace Temptation": 1
			},
			"selectedDeck": [],
			"money": 0,
			"packs": 1
		}
		
		#for testers
		testers = ['135526460881502209','128216983605870603']
		if ctx.message.author.id in testers:
			playerData['collection'] = {}
			for files in os.listdir('./cards'):
				playerData['collection'][files[:-3]] = 4
		
		with open('player_data/'+str(playerID)+'.txt', 'w') as outfile:
			json.dump(playerData, outfile)
		
		yield from self.bot.say( "Registration successful!" )

		
def setup(bot):
	bot.add_cog(InfoCommands(bot))
