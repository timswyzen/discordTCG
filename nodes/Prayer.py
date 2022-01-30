#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Prayer"
DESC = "At the start of your turn, heal 1 lifeforce for each Node you control."
ENERGY = -2
TRIGGER = None

#What happens when you play it
async def playFunc(ply,enemy):
	await mechanics.heal( ply, len(ply.nodes) )
	return
	
async def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
async def deathFunc(ply,enemy):
	return
	
#What happens when the TRIGGER is triggered
async def triggerFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )
