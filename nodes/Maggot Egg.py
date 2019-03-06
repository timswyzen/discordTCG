#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Maggot Egg"
DESC = "At the start of your turn, sacrifice this Node and spawn a Parasite Node."
ENERGY = 0
TRIGGER = None

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	mechanics.sacNode( ply, enemy, ply.nodes.index( 'Maggot Egg' ) )
	ply.addNode( 'Parasite' )
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
