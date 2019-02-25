#!/user/bin/env python

import time

class TCGame:

	def __init__(self, challenger, defender, wager):
		self.challenger = challenger
		self.defender = defender
		self.chalObj = None #object for challenger
		self.defObj = None #object for defender
		self.wager = wager
		self.startTime = time.time()
		self.gameMessage = None
		
	def __str__(self):
		return( self.challenger + " (HP: " + str(self.chalObj.lifeforce) + ") challenging " + self.defender + " (HP: " + str(self.defObj.lifeforce) + ")." )
