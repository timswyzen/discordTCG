#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Tempter"
DESC = "Passively increases your desperation and hunger by 10."
ENERGY = -6
TRIGGER = None

#What happens when you play it
def playFunc(ply,enemy):
	return
	
def oneTimeFunc(ply,enemy):
	ply.desperation += 10
	ply.hunger += 10
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	ply.desperation -= 10
	ply.hunger -= 10
	
#What happens when the TRIGGER is triggered
def triggerFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )
