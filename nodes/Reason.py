#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Reason"
DESC = "You can't mill cards."
ENERGY = -1
TRIGGER = None

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	ply.milled = True
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
