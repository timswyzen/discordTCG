#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Neuron"
DESC = "At the start of your turn, draw a card."
ENERGY = -4

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	ply.drawCard()
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

