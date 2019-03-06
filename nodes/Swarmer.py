#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Swarmer"
DESC = "At the start of your turn, deal 1 damage to your opponent for each Swarmer you control."
ENERGY = -3
TRIGGER = None

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	yield from mechanics.damage( enemy, ply.nodes.count('Swarmer') )
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
