#!/user/bin/env python
from typing import List

from classes.NodeFunction import NodeFunction


class GameNode:
	#Set up the Node object
	def __init__(self, name, description, energy, func_list: List[NodeFunction]):
		self.name = name
		self.desc = description
		self.energy = energy
		self.funcs = func_list
		
	def __str__(self):
		return "**" + self.name + " ("+str(self.energy)+")**: " + self.desc
