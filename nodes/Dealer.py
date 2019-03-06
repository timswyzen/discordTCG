#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Dealer"
DESC = "Whenever a friendly Node is destroyed, if it was a Drugged Node, spawn another one."
ENERGY = -1
TRIGGER = "SAC"

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
def triggerFunc(ply,enemy,data,affectedPlayer):
	if affectedPlayer == "friendly":
		if data.name == "Drugged":
			ply.addNode( 'Drugged' )
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )

