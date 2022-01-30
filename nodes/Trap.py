#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Trap"
DESC = "When destroyed, deal 3 damage to your opponent."
ENERGY = 0
TRIGGER = None

#What happens when you play it
async def playFunc(ply,enemy):
	return
	
async def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
async def deathFunc(ply,enemy):
	await mechanics.damage( enemy, 3 )
	
#What happens when the TRIGGER is triggered
async def triggerFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )
