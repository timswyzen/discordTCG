#!/user/bin/env python

#import mechanics

class Card:
	#Set up the card object
	def __init__(self, name, cost, rarity, description, targets, cardtype, ability):
		self.name = name
		self.cost = cost
		self.rarity = rarity
		self.func = ability
		self.targets = targets
		self.desc = description
		self.cardtype = cardtype
		
	def __str__(self):
		return "**" + self.name + " (" + str(self.cost) + ")** *" + self.rarity + "* : " + self.desc
