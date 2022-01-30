#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Pressure"
DESC = "At the start of your turn, deal 1 damage to your opponent."
ENERGY = -1
TRIGGER = None

#What happens when you play it
async def playFunc(ply,enemy):
	await mechanics.damage( enemy, 1 )
	
async def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
async def deathFunc(ply,enemy):
	return
	
#What happens when the TRIGGER is triggered
async def triggerFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )
