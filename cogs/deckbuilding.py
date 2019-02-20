#!/user/bin/env python
import discord
from discord.ext import commands
import asyncio, json, os
from mechanics import cardList, getPlyData
from collections import Counter

class Deckbuilding():
	def __init__(self, bot):
		self.bot = bot
		
	#Get your decklist
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def getlist( self, ctx, *args ):
		"""Gets your decklist. Use this to save and modify lists. Try doing this in DMs."""
		stringToPrint = ""
		i=0
		selectedDeck = getPlyData(ctx.message.author)['selectedDeck']
		for key,val in Counter(selectedDeck).items():
			stringToPrint = stringToPrint + ( str(val) + "x " + key + "\n" )
			i+=1
			if i>=10:
				i=0
				yield from self.bot.say( stringToPrint )
				stringToPrint = ""
		if not stringToPrint == "":
			yield from self.bot.say( stringToPrint )
		yield from self.bot.say( str(len(selectedDeck)) + " cards in deck." )
		
	#Get your collection
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def collection( self, ctx, *args ):
		"""Gets your collection. Try doing this in DMs."""
		stringToPrint = ""
		i=0
		for key,val in getPlyData( ctx.message.author )['collection'].items():
			stringToPrint = stringToPrint + ( str(val) + "x " + str(cardList[key.lower()]) + "\n" )
			i+=1
			if i>=10:
				i=0
				yield from self.bot.say( stringToPrint )
				stringToPrint = ""
		yield from self.bot.say( stringToPrint )
		
	#Clears your deck
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def clear( self, ctx, *args ):
		"""Removes all cards from your current deck."""
		try:
			deckList = getPlyData( ctx.message.author )['selectedDeck']
		except:
			yield from self.bot.say( "You aren't registered yet. Type =register" )
			return
			
		deckList = []
		with open('player_data/'+str(ctx.message.author.id)+'.txt', 'r') as json_file: 
			fileContents = json.loads(json_file.read())
		fileContents['selectedDeck'] = deckList
		with open('player_data/'+str(ctx.message.author.id)+'.txt', 'w') as outfile:
			json.dump(fileContents, outfile)
			
		yield from self.bot.say( "Successfully cleared your current decklist." )
		
	#Remove an amount of a card from your deck
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def remove( self, ctx, *args ):
		"""<amt> <card> to remove cards from your deck."""
		#Syntax
		try:
			card = ' '.join(args[1:])
			amt = int(args[0])
		except:
			yield from self.bot.say( "Incorrect syntax. =remove <cardname> <amount>" )
			return
			
		#Make sure they're registered
		try:
			deck = Counter(getPlyData( ctx.message.author )['selectedDeck'])
			deckList = getPlyData( ctx.message.author )['selectedDeck']
		except:
			yield from self.bot.say( "You aren't registered yet. Type =register" )
			return
			
		#Make sure we have the card to remove
		cardPair = None
		for item in deck.items():
			if card.lower() == item[0].lower():
				cardPair = item
				
		if cardPair == None:
			yield from self.bot.say( "This card isn't in your deck." )
			return
		if cardPair[1] < amt:
			yield from self.bot.say( "You don't have that many of that card in your deck." )
			return
			
		#Remove the card
		for _ in range( amt ):
			deckList.remove( cardPair[0] )
			
		#Save
		with open('player_data/'+str(ctx.message.author.id)+'.txt', 'r') as json_file: 
			fileContents = json.loads(json_file.read())
		fileContents['selectedDeck'] = deckList
		with open('player_data/'+str(ctx.message.author.id)+'.txt', 'w') as outfile:
			json.dump(fileContents, outfile)
			
		yield from self.bot.say( "Successfully removed card(s) from your current deck." )
	
	#Bulk add cards to your deck
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def bulkadd( self, ctx, *args ):
		"""Add many cards to your deck at once."""
		#user interaction
		yield from self.bot.say( "On each line, write <number>x <cardname>. For example:\n2x Caltrops\n1x Ambush" )
		message = yield from self.bot.wait_for_message( author=ctx.message.author, timeout=90 )
		
		#parsing
		messageList = message.content.split( '\n' )
		for idx,line in enumerate(messageList):
			messageList[idx] = line.split( 'x ' )
		
		#has data check + data retrieval
		try:
			collection = getPlyData( ctx.message.author )['collection']
			deckList = getPlyData( ctx.message.author )['selectedDeck']
		except:
			yield from self.bot.say( "You aren't registered yet. Type =register" )
			return
			
		for cardEntry in messageList: #for each [2, "caltrops"], for example
			cardPair = None
			#formatting and data getting
			try:
				for item in collection.items():
					if cardEntry[1].lower() == item[0].lower():
						cardPair = item
			except:
				yield from self.bot.say( "Invalid format!" )
				return
			
			#checks
			if cardPair == None:
				yield from self.bot.say( cardEntry[1] + " isn't in your collection." )
				return
			if cardPair[1] < int(cardEntry[0]):
				yield from self.bot.say( "You don't have that many "+cardEntry[1]+" in your collection." )
				return
			if Counter(deckList)[cardPair[0]] + int(cardEntry[0]) > 4:
				yield from self.bot.say( "You can only have 4 of a card in your deck. ("+cardPair[0]+")" )
				return
				
			#actually add it
			for _ in range( int(cardEntry[0]) ):
				deckList.append( cardPair[0] )
			
		#save
		with open('player_data/'+str(ctx.message.author.id)+'.txt', 'r') as json_file: 
			fileContents = json.loads(json_file.read())
		fileContents['selectedDeck'] = deckList
		with open('player_data/'+str(ctx.message.author.id)+'.txt', 'w') as outfile:
			json.dump(fileContents, outfile)
			
		yield from self.bot.say( "Successfully added card(s) to your current deck." )
			
	
	#Add an amount of a card to your deck
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def add( self, ctx, *args ):
		"""<amt> <card> to add cards to your deck."""
		#Syntax
		try:
			card = ' '.join(args[1:])
			amt = int(args[0])
		except:
			yield from self.bot.say( "Incorrect syntax. =add <cardname> <amount>" )
			return
			
		#Make sure they're registered
		try:
			collection = getPlyData( ctx.message.author )['collection']
			deckList = getPlyData( ctx.message.author )['selectedDeck']
		except:
			yield from self.bot.say( "You aren't registered yet. Type =register" )
			return
			
		#Make sure we have the card to add 
		cardPair = None
		for item in collection.items():
			if card.lower() == item[0].lower():
				cardPair = item
			
		if cardPair == None:
			yield from self.bot.say( "This card isn't in your collection." )
			return
		if cardPair[1] < amt:
			yield from self.bot.say( "You don't have that many of that card in your collection." )
			return
		if Counter(deckList)[cardPair[0]] + amt > 4:
			yield from self.bot.say( "You can only have 4 of a card in your deck." )
			return
			
		#Add the card
		for _ in range( amt ):
			#TODO: Check for card limits
			deckList.append( cardPair[0] )
			
		#Save
		with open('player_data/'+str(ctx.message.author.id)+'.txt', 'r') as json_file: 
			fileContents = json.loads(json_file.read())
		fileContents['selectedDeck'] = deckList
		with open('player_data/'+str(ctx.message.author.id)+'.txt', 'w') as outfile:
			json.dump(fileContents, outfile)
			
		yield from self.bot.say( "Successfully added card(s) to your current deck." )
	
	#Set your entire deck list (TODO)
	
	
	
def setup(bot):
	bot.add_cog(Deckbuilding(bot))
