#!/user/bin/env python
import random

class Player:

	def __init__(self, name, deck, hand):
		self.name = name
		self.deck = deck #last element of deck is the top of the deck (next to draw)
		self.hand = hand
		self.lifeforce = 20
		self.active = False
		self.nodes = []
		self.maxNodes = 6
		self.energy = 1
		self.eotEffects = []
		self.milled = False #if they already used 'mill' this turn
		self.hunger = 1 #Rate of lifegain from sacrificing nodes
		self.desperation = 1 #Rate of lifegain from milling
		
	#Custom function in case I end up wanting to do something with shuffling (e.g hooks)
	def shuffle(self):
		random.shuffle( self.deck )
		
	def newTurn(self):
		self.eotEffects = []
		self.milled = False
		self.active = False
		
	def drawCard(self):
		#mill out
		if len(self.deck) <= 0:
			return False
		self.hand.append( self.deck.pop() )
		return True
		
	def addNode(self, nodeName, enerCost): #TODO: figure out a way to not need enerCost
		if len(self.nodes) >= self.maxNodes:
			return False
		else:
			self.nodes.append(nodeName)
			self.energy = self.energy + enerCost
			
	def removeNode(self, nodeName, enerCost):
		for node in self.nodes:
			if nodeName.lower() == node:
				self.nodes.remove( nodeName )
				break
		self.energy = self.energy - enerCost
			
	def __str__(self):
		return "[--"+self.name+"--]\nHP: "+str(self.lifeforce)+"\nEnergy: "+ str(self.energy) +"\nCards in hand: "+str(len(self.hand))+"\nNodes: "+str(self.nodes)+"\nHunger: "+str(self.hunger)
