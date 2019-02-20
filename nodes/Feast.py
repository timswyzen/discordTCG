#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Feast"
DESC = "Players can't gain lifeforce from sacrificing Nodes."
ENERGY = 1

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

