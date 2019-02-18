#!/user/bin/env python

class TCGame:

	def __init__(self, challenger, defender):
		self.challenger = challenger
		self.defender = defender
		self.chalObj = None #object for challenger
		self.defObj = None #object for defender
		
	def __str__(self):
		return( self.challenger + " (HP: " + str(self.chalObj.lifeforce) + ") challenging " + self.defender + " (HP: " + str(self.defObj.lifeforce) + ")." )
