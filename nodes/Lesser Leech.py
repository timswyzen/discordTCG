#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Lesser Leech"
DESC = "At the end of your turn, deal 2 damage to your opponent. Gain lifeforce equal to the damage dealt."
ENERGY = -1
TRIGGER = None

#What happens when you play it
def playFunc(ply,enemy):
	yield from mechanics.damage( enemy, 2 )
	yield from mechanics.heal( ply, 2 )
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
