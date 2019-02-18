#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Tempter"
DESC = "Passively increases your desperation and hunger by 2."
ENERGY = -3

#What happens when you play it
def playFunc(ply,enemy):
	ply.desperation = ply.desperation + 2
	ply.hunger = ply.hunger + 2
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	ply.desperation = ply.desperation - 2
	ply.hunger = ply.hunger - 2
	
addNode( NAME, DESC, playFunc, ENERGY, deathFunc )

