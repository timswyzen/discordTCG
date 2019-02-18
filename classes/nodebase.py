#!/user/bin/env python

class GameNode:
	#Set up the Node object
	def __init__(self, name, description, ability, energy, deathAbility):
		self.name = name
		self.func = ability #should trigger start of your turn
		self.desc = description
		self.energy = energy
		self.deathFunc = deathAbility
		
	def __str__(self):
		return self.name + " ("+str(self.energy)+"): " + self.desc
