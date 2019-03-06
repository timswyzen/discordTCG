#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Prayer"
DESC = "At the start of your turn, heal 1 lifeforce for each Node you control."
ENERGY = -2
TRIGGER = None

#What happens when you play it
def playFunc(ply,enemy):
	yield from mechanics.heal( ply, len(ply.nodes) )
	return
	
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
#What happens when the TRIGGER is triggered
def triggerFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )
