#!/user/bin/env python
import random
from mechanics import nodeETB, sacNode, gameTrigger

class Player:

	def __init__(self, name, deck, hand, bot, ctx):
		self.name = name
		self.deck = deck #last element of deck is the top of the deck (next to draw)
		self.hand = hand
		self.bot = bot #so the bot can do its thing
		self.ctx = ctx #so the bot can do its thing
		self.energy = 2
		self.lifeforce = 50
		self.active = False
		self.nodes = []
		self.log = []
		self.maxNodes = 6
		self.eotEffects = []
		self.nodesToTrigger = [] #ugh. triggers all nodes later cause yield from is DUMB.
		self.milled = False #if they already used 'mill' this turn
		self.playedNode = False #if they already played a node this turn
		self.hunger = 10 #Rate of lifegain from sacrificing nodes (/10)
		self.desperation = 10 #Rate of lifegain from milling (/10)
		self.opponent = None #just so we have this stored without needing dumb imports
		self.lastHandDM = None #for better hand DMing
		self.cardsThisTurn = 0 #spells played this turn
		"""Card-specific variables (TODO: Find a better alternative)"""
		self.mindSwap = False
		self.desperationBoost = 0 #reset desperation boost (subtract this at start of turn)
		self.opponentCantSpawnNodes = False
		
	#Custom function in case I end up wanting to do something with shuffling (e.g hooks)
	def shuffle(self):
		random.shuffle( self.deck )
		
	def addMaxNodes(self, amt):
		#set
		self.maxNodes += amt
		if self.maxNodes > 10:
			self.maxNodes = 10
		if self.maxNodes < 0:
			self.maxNodes = 0
		#kill excess nodes
		while len(self.nodes) > self.maxNodes:
			sacNode( ply, self.opponent, self.nodes[self.maxNodes] )
		
		
	def newTurn(self):
		self.eotEffects = []
		self.active = False
		self.playedNode = False
		if self.hunger < 0:
			self.hunger = 0
		if self.desperation < 0:
			self.desperation = 0
		self.cardsThisTurn = 0
		
	def newMyTurn(self):
		self.milled = False
		self.active = True
		"""Card specific steps (TODO: Find a better alternative)"""
		if self.mindSwap: #Mind Swap
			self.desperation, self.opponent.desperation = self.opponent.desperation, self.desperation
			self.hunger, self.opponent.hunger = self.opponent.hunger, self.hunger
			self.mindSwap = False
		if not self.desperationBoost == 0:
			self.desperation -= self.desperationBoost
			self.desperationBoost = 0
		self.opponentCantSpawnNodes = False
		gameTrigger( "NEW_TURN", self, None )
		
	def drawCard(self):
		#mill out
		if len(self.deck) <= 0:
			return False
		self.hand.append( self.deck.pop() )
		return True
		gameTrigger( "DRAW", self, None )
		
	def randomDiscard(self):
		if len(self.hand) > 0:
			discarded = self.hand.pop( random.randint(0,len(self.hand)-1) )
		gameTrigger( "DISCARD", self, discarded )
		
	def addNode(self, nodeName): #TODO: possibly move to mechanics.py for consistency with sacNode()
		if self.opponent.opponentCantSpawnNodes:
			return
		gameTrigger( "NODESPAWN", self, nodeName )
		if len(self.nodes) >= self.maxNodes:
			sacNode( self, self.opponent, self.maxNodes-1 )
		self.nodes.insert(0, nodeName)
		nodeETB( self, nodeName )
		
		
	def burn(self, amt): #Milling without lifeforce gain
		burnedCards = []
		for i in range(amt):
			if len(self.deck) > 0:
				burnedCards.append( self.deck.pop() )
		gameTrigger( "BURN", self, burnedCards )
			
	def removeNode(self, nodeName, enerCost):
		for node in self.nodes:
			if nodeName.lower() == node:
				self.nodes.remove( nodeName )
				break
		self.energy = self.energy - enerCost
			
	def __str__(self):
		#return "[--"+self.name+"--]\nHP: "+str(self.lifeforce)+"\nEnergy: "+ str(self.energy) +"\nCards in hand: "+str(len(self.hand))+"\nCards in deck: "+str(len(self.deck))+"\nNodes: "+str(self.nodes)+"\nHunger: "+str(self.hunger)+"\nDesperation: "+str(self.desperation)
		return ("[--- :crossed_swords: **"+self.name.upper()+"** :crossed_swords: ---]\n" +
			":heart: LF: *"+str(self.lifeforce)+" ("+str(self.energy)+" energy)*\n" +
			":flower_playing_cards: Cards in hand: *" + str(len(self.hand)) + " (+" + str(len(self.deck)) + " deck)*\n" +
			":gear: Nodes: *" + str(self.nodes) + "*\n" + 
			":green_apple: Hunger: *" + str(self.hunger) + "*\n" + 
			":hourglass: Desperation: *" + str(self.desperation) + "*")
