#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Tempter"
DESC = "Passively increases your desperation and hunger by 10."
ENERGY = -6

#What happens when you play it
def playFunc(ply,enemy):
	return
	
def oneTimeFunc(ply,enemy):
	ply.desperation += 10
	ply.hunger += 10
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	ply.desperation -= 10
	ply.hunger -= 10
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

