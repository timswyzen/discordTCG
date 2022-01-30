#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Parasite"
DESC = "At the start of your turn, spawn a Maggot Egg Node."
ENERGY = -1
TRIGGER = None

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	yield from ply.addNode( 'Maggot Egg' )
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
#What happens when the TRIGGER is triggered
def triggerFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )
