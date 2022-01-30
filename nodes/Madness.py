#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Madness"
DESC = "Whenever your opponent discards a card, draw a card."
ENERGY = -1
TRIGGER = "DISCARD"

#What happens when you play it (at the start of your turn)
async def playFunc(ply,enemy):
	return
	
#Abilities that only happens when the Node is spawned
async def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
async def deathFunc(ply,enemy):
	return
	
#What happens when the TRIGGER is triggered
async def triggerFunc(ply,enemy,discarded,affectedPlayer):
	if affectedPlayer == "enemy":
		await ply.drawCard()
	else:
		return False
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )

