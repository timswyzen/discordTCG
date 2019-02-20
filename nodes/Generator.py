#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Generator"
DESC = "Grants 1 energy."
ENERGY = 1

#What happens when you play it
def playFunc(ply,enemy):
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

