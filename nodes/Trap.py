#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Trap"
DESC = "When destroyed, deal 3 damage to your opponent."
ENERGY = 0
TRIGGER = None

#What happens when you play it
def playFunc(ply,enemy):
	return
	
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	yield from mechanics.damage( enemy, 3 )
	
#What happens when the TRIGGER is triggered
def triggerFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )
