#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Gluttony"
DESC = "At the start of your turn, decrease your opponent's Hunger by 10."
ENERGY = -4

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	enemy.hunger = enemy.hunger - 10
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

