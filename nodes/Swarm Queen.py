#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Swarm Queen"
DESC = "At the start of your turn, deal 3 damage to your opponent for each Swarmer Node you control."
ENERGY = -4
TRIGGER = None

#What happens when you play it (at the start of your turn)
async def playFunc(ply,enemy):
	await mechanics.damage( enemy, 3*ply.nodes.count('Swarmer') )
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
