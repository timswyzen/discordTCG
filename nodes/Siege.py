#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Siege"
DESC = "At the start of your turn, increase your opponent's Desperation and Hunger by 5."
ENERGY = 2
TRIGGER = None

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	enemy.hunger += 5
	enemy.desperation += 5
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

