#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Blood"
DESC = "Whenever you damage your opponent, heal that much lifeforce."
ENERGY = -3
TRIGGER = "DAMAGE"

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
#What happens when the TRIGGER is triggered
def triggerFunc(ply,enemy,dataPassed,affectedPlayer):
	#dataPassed is damage dealt
	if affectedPlayer == "enemy":
		yield from mechanics.heal( ply, dataPassed )
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )

