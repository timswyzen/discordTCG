#!/user/bin/env python

class GameNode:
	#Set up the Node object
	def __init__(self, name, description, ability, oneTimeAbility, energy, deathAbility, triggerType, triggerFunc):
		self.name = name
		self.func = ability #should trigger start of your turn
		self.spawnFunc = oneTimeAbility
		self.desc = description
		self.energy = energy
		self.deathFunc = deathAbility
		self.triggerType = triggerType
		self.triggerFunc = triggerFunc
		
	def __str__(self):
		return self.name + " ("+str(self.energy)+"): " + self.desc
