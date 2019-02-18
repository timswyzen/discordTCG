#!/user/bin/env python
import discord
from discord.ext import commands
import asyncio, json, os
from mechanics import cardList, nodeList

"""Extra commands that didn't need to be in the base file"""

class InfoCommands():
	def __init__(self, bot):
		self.bot = bot
		
	#Get Node information (TODO: move to utility cog)
	@commands.command(pass_context=True)	
	@asyncio.coroutine
	def node( self, ctx, *args ):
		"""Query the bot for information on a Node."""
		try:
			if args[0].lower() in nodeList:
				yield from self.bot.say( str( nodeList[args[0].lower()] ) )
			else:
				yield from self.bot.say( "Card not found." )
		except Exception as e:
			print(e)
	
	#Get card information (TODO: move to utility cog)
	@commands.command(pass_context=True)	
	@asyncio.coroutine
	def card( self, ctx, *args ):
		"""Query the bot for information on a card."""
		try:
			if args[0].lower() in cardList:
				yield from self.bot.say( str( cardList[args[0].lower()] ) )
			else:
				yield from self.bot.say( "Card not found." )
		except Exception as e:
			print(e)
			
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
			"selectedDeck": ['Swing','Get Puncher','Recursion','Voracity', 'Desperation', 'Desperation', 'Embrace Temptation'], #TODO: put actual cards in default deck
			"money": 0,
		}
		with open('player_data/'+str(playerID)+'.txt', 'w') as outfile:
			json.dump(playerData, outfile)
		
		yield from self.bot.say( "Registration successful!" )

		
def setup(bot):
	bot.add_cog(InfoCommands(bot))
