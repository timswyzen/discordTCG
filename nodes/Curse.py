#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Curse"
DESC = "At the start of your turn, burn 4 cards."
ENERGY = 0

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	ply.burn(4)
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

