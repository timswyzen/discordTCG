#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Hope"
DESC = "At the start of your turn, decrease your opponent's Desperation by 5."
ENERGY = -4
TRIGGER = None

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	enemy.desperation -= 5
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
