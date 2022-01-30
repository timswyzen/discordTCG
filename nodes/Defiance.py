#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Defiance"
DESC = "Whenever your opponent spawns a Node, deal 3 damage to them."
ENERGY = -1
TRIGGER = "NODESPAWN"

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
async def triggerFunc(ply,enemy,data,affectedPlayer):
	if affectedPlayer == "enemy":
		await mechanics.damage( enemy, 3 )
	else:
		return False
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )

