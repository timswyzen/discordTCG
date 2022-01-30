#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Fountain"
DESC = "When this Node spawns or is destroyed, draw a card."
ENERGY = 0
TRIGGER = None

#What happens when you play it (at the start of your turn)
async def playFunc(ply,enemy):
	return
	
#Abilities that only happens when the Node is spawned
async def oneTimeFunc(ply,enemy):
	await ply.drawCard()
	return
	
#What happens when it's sacrificed/killed
async def deathFunc(ply,enemy):
	await ply.drawCard()
	return
	
#What happens when the TRIGGER is triggered
async def triggerFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )

