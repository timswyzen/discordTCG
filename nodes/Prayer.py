#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Prayer"
DESC = "Gain 1 extra lifeforce from energy for each Node you control."
ENERGY = -2

#What happens when you play it
def playFunc(ply,enemy):
	return
	
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

