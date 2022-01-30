#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Scrambler Trap"
DESC = "When this Node dies, your opponent discards two cards at random."
ENERGY = -1
TRIGGER = None

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	yield from enemy.randomDiscard()
	yield from enemy.randomDiscard()
	return
	
#What happens when the TRIGGER is triggered
def triggerFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )
