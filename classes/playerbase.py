#!/user/bin/env python
import random
from mechanics import nodeETB, sacNode

class Player:

	def __init__(self, name, deck, hand):
		self.name = name
		self.deck = deck #last element of deck is the top of the deck (next to draw)
		self.hand = hand
		self.energy = 2
		self.lifeforce = 35
		self.active = False
		self.nodes = []
		self.maxNodes = 6
		self.eotEffects = []
		self.milled = False #if they already used 'mill' this turn
		self.playedNode = False #if they already played a node this turn
		self.hunger = 10 #Rate of lifegain from sacrificing nodes (/10)
		self.desperation = 10 #Rate of lifegain from milling (/10)
		self.opponent = None #just so we have this stored without needing dumb imports
		self.lastHandDM = None #for better hand DMing
		self.cardsThisTurn = 0 #spells played this turn
		"""Card-specific variables (TODO: Find a better alternative)"""
		self.mindSwap = False
		
	#Custom function in case I end up wanting to do something with shuffling (e.g hooks)
	def shuffle(self):
		random.shuffle( self.deck )
		
	def newTurn(self):
		self.eotEffects = []
		self.milled = False
		self.active = False
		self.playedNode = False
		if self.hunger < 0:
			self.hunger = 0
		if self.desperation < 0:
			self.desperation = 0
		self.cardsThisTurn = 0
		"""Card specific steps (TODO: Find a better alternative)"""
		if self.mindSwap: #Mind Swap
			self.desperation, self.opponent.desperation = self.opponent.desperation, self.desperation
			self.hunger, self.opponent.hunger = self.opponent.hunger, self.hunger
			self.mindSwap = False
		
	def drawCard(self):
		#mill out
		if len(self.deck) <= 0:
			return False
		self.hand.append( self.deck.pop() )
		return True
		
	def addNode(self, nodeName): #TODO: possibly move to mechanics.py for consistency with sacNode()
		if len(self.nodes) >= self.maxNodes:
			#sacNode( ply, self.opponent, random.randint(0,len(self.nodes)) ) #TODO: notify users what died and enable this feature
			return False
		self.nodes.append(nodeName)
		nodeETB( self, nodeName )
		
	def burn(self, amt): #Milling without lifeforce gain
		for i in range(amt):
			if len(self.deck) > 0:
				self.deck.pop()
			
	def removeNode(self, nodeName, enerCost):
		for node in self.nodes:
			if nodeName.lower() == node:
				self.nodes.remove( nodeName )
				break
		self.energy = self.energy - enerCost
			
	def __str__(self):
		return "[--"+self.name+"--]\nHP: "+str(self.lifeforce)+"\nEnergy: "+ str(self.energy) +"\nCards in hand: "+str(len(self.hand))+"\nCards in deck: "+str(len(self.deck))+"\nNodes: "+str(self.nodes)+"\nHunger: "+str(self.hunger)+"\nDesperation: "+str(self.desperation)
		
