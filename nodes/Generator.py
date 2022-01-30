#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Generator"
DESC = "Grants 1 energy."
ENERGY = 1
TRIGGER = None

#What happens when you play it
async def playFunc(ply,enemy):
	return
	
#Abilities that only happens when the Node is spawned
async def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
async def deathFunc(ply,enemy):
	return
	
#What happens when the TRIGGER is triggered
async def triggerFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )
