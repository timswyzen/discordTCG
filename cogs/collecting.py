#!/user/bin/env python
import discord
from discord.ext import commands
import asyncio, json, os, random
from mechanics import cardList, getPlyData, grantCard, grantMoney, grantPacks, getBal, getPacks

class Collecting():
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def openpack( self, ctx, *args ):
		"""OPEN A SHINY NEW PACK!"""
		if getPacks( ctx.message.author.id ) < 1:
			yield from self.bot.say( "You don't have any packs to open :( Buy some with =buy!" )
			return
		commons, uncommons, rares = [], [], []
		cardsReceived = []
		for card in cardList:
			if cardList[card].rarity == 'C':
				commons.append( cardList[card].name )
			elif cardList[card].rarity == 'U':
				uncommons.append( cardList[card].name )
			elif cardList[card].rarity == 'R':
				rares.append( cardList[card].name )
		
		stringToSay = ( ":star: :star2: :star2: :star2: :star2: :star2: :star2: :star2: :star2: :star2: :star:\n:star: :confetti_ball:           You got new cards!           :confetti_ball: :star:\n" )
		
		for i in range( 5 ):
			#TODO: can't get 5+ of the same card
			cardsReceived.append( random.choice( commons ) )
			stringToSay += ":star: Common: " + cardsReceived[i] + "\n"
		for i in range( 2 ):
			cardsReceived.append( random.choice( uncommons ) )
			stringToSay += ":star: Uncommon: " + cardsReceived[i+5] + "\n"
		cardsReceived.append( random.choice( rares ) )
		stringToSay += ":star: :star: **RARE: " + cardsReceived[7] + "**\n"
		stringToSay += ":star: :star2: :star2: :star2: :star2: :star2: :star2: :star2: :star2: :star2: :star:"
		
		yield from self.bot.say( stringToSay )
		
		for card in cardsReceived:
			grantCard( ctx.message.author.id, card, 1 )

		grantPacks( ctx.message.author.id, -1 )
		
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def packs( self, ctx, *args ):
		"""Get how many packs you have."""
		yield from self.bot.say( "You currently have " + str(getPacks(ctx.message.author.id)) + " pack(s)." )
		
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def buy( self, ctx, amt: int = 1 ):
		"""Buy some packs! =buy <amount>"""
		if amt < 1:
			yield from self.bot.say( "Invalid input." )
			return
		if getBal( ctx.message.author.id ) < amt * 150:
			yield from self.bot.say( "Not enough money for " + str(amt) + " packs." )
			return
		grantPacks( ctx.message.author.id, amt )
		if amt == 1:
			yield from self.bot.say( "Bought a pack! Open it with =openpack." )
		else:
			yield from self.bot.say( "Bought " + amt + " packs!!!! Open them with =openpack!!!!!!!" )
		
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def bal( self, ctx, *args ):
		"""Get your current $ balance."""
		yield from self.bot.say( "You currently have $" + str(getBal(ctx.message.author.id)) + "." )
		
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def trade( self, ctx, target: discord.Member = None, *args ):
		"""Trade with another user. =select <@ user>"""
		if ctx.message.author == target:
			yield from self.bot.say( "Why would you trade with yourself? :confounded:" )
			return
		trader, tradee = [], []
		yield from self.bot.say( "Type 'quit' at any time to quit the trade menu." )
		yield from self.bot.say( "What are you offering? Syntax: <amount>x <card> or $<money amount>. For example:\n2x Voracity\n$20" )
		message = yield from self.bot.wait_for_message( author=ctx.message.author, timeout=90 )
		if message.content.lower().startswith('quit'):
			yield from self.bot.say( "Quit the trade menu." )
			return
		
		#Setting up data for trader's offerings
		messageList = message.content.split( '\n' )
		for idx,line in enumerate(messageList):
			messageList[idx] = line.split( 'x ' )
			
		#has data check + data retrieval
		try:
			playerData = getPlyData(ctx.message.author)
		except:
			yield from self.bot.say( "You aren't registered yet. Type =register" )
			return
			
		for cardEntry in messageList: #for each [2, "caltrops"], for example
			cardPair = None
			#formatting and data getting
			if cardEntry[0][0] == '$':
				with open('player_data/'+str(ctx.message.author.id)+'.txt', 'r') as json_file: 
					traderMoney = json.loads(json_file.read())['money']
				if traderMoney < int(cardEntry[0][1:]) or int(cardEntry[0][1:]) < 0:
					yield from self.bot.say( "You don't have enough money." )
					return
				trader.append( cardEntry[0][1:] )
			else:	
				try:
					for item in playerData['collection'].items():
						if cardEntry[1].lower() == item[0].lower():
							cardPair = item
				except:
					yield from self.bot.say( "Invalid format!" )
					return
					
				if cardPair == None:
					yield from self.bot.say( cardEntry[1] + " isn't in your collection." )
					return
				if cardPair[1] < int(cardEntry[0]):
					yield from self.bot.say( "You don't have that many "+cardEntry[1]+" in your collection." )
					return
				
				trader.append(cardEntry)
		
		yield from self.bot.say( "What do you want in return? (same syntax)" )
		message = yield from self.bot.wait_for_message( author=ctx.message.author, timeout=90 )
		if message.content.lower().startswith('quit'):
			yield from self.bot.say( "Quit the trade menu." )
			return
		
		#Setting up data for trader's offerings
		messageList = message.content.split( '\n' )
		for idx,line in enumerate(messageList):
			messageList[idx] = line.split( 'x ' )
			
		#has data check + data retrieval
		try:
			playerData = getPlyData(target)
		except:
			yield from self.bot.say( "Target isn't registered yet." )
			return
			
		for cardEntry in messageList: #for each [2, "caltrops"], for example
			cardPair = None
			#formatting and data getting
			if cardEntry[0][0] == '$':
				with open('player_data/'+str(target.id)+'.txt', 'r') as json_file: 
					tradeeMoney = json.loads(json_file.read())['money']
				if tradeeMoney < int(cardEntry[0][1:]) or int(cardEntry[0][1:]) < 0:
					yield from self.bot.say( "He or she doesn't have enough money." )
					return
				tradee.append( cardEntry[0][1:] )
			else:	
				try:
					for item in playerData['collection'].items():
						if cardEntry[1].lower() == item[0].lower():
							cardPair = item
				except:
					yield from self.bot.say( "Invalid format!" )
					return
					
				if cardPair == None:
					yield from self.bot.say( cardEntry[1] + " isn't in your collection." )
					return
				if cardPair[1] < int(cardEntry[0]):
					yield from self.bot.say( "You don't have that many "+cardEntry[1]+" in your collection." )
					return
				
				tradee.append(cardEntry)
		#wow that was a lot. let's get the other user's approval then do the trade now.
		print(str(trader) + " | " + str(tradee))
		def check(msg):
			print('checking')
			return msg.content.lower().startswith('yes') or msg.content.lower().startswith('no')
		yield from self.bot.say(  target.name + ": Do you accept the above trade? ('yes' or 'no')" )
		message = yield from self.bot.wait_for_message( author=target, check=check, timeout=30 )
		if message.content.lower().startswith('no'):
			yield from self.bot.say( "Trade request denied." )
			return
		elif message.content.lower().startswith('yes'):
			#give trader the tradee's stuff
			for item in tradee:
				if isinstance( item, str ):
					grantMoney( ctx.message.author.id, int(item) )
					grantMoney( target.id, -1*int(item) )
				else:
					grantCard( target.id, item[1], -1*int(item[0]) )
					grantCard( ctx.message.author.id, item[1], item[0] )
			#give tradee the trader's stuff
			for item in trader:
				if isinstance( item, str ):
					grantMoney( ctx.message.author.id, -1*int(item) )
					grantMoney( target.id, int(item) )
				else:
					grantCard( target.id, item[1], item[0] )
					grantCard( ctx.message.author.id, item[1], -1*int(item[0]) )
			yield from self.bot.say( "Trade complete!" )

def setup(bot):
	bot.add_cog(Collecting(bot))
