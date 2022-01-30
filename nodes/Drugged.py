#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Drugged"
DESC = "When this is spawned, draw a card. When it's destroyed, lose 2 energy and discard a random card."
ENERGY = 4
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
	ply.energy -= 2
	await ply.randomDiscard()
	return
	
#What happens when the TRIGGER is triggered
async def triggerFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )

