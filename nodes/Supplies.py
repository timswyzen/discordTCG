#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Supplies"
DESC = "When destroyed, gain 5 lifeforce."
ENERGY = 0

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	ply.lifeforce += 5
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

