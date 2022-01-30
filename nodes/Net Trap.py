#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics, random

#Simple variables
NAME = "Net Trap"
DESC = "When this is destroyed, steal a random enemy Node."
ENERGY = -2
TRIGGER = None

#What happens when you play it (at the start of your turn)
async def playFunc(ply,enemy):
	return
	
#Abilities that only happens when the Node is spawned
async def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
async def deathFunc(ply,enemy):
	if len(enemy.nodes) > 0:
		target = random.randint( 0, len(enemy.nodes)-1 )
		nodeType = mechanics.nodeList[enemy.nodes[target].lower()]
		await ply.addNode( enemy.nodes[target] )
		enemy.energy -= nodeType.energy
		enemy.nodes.pop( target )
	return
	
"""What happens when the TRIGGER is triggered. 
If it was triggered by owner, affectedPlayer is "friendly"
If it was triggered by the enemy, affectedPlayer is "enemy"
data is whatever data is relevant to the trigger, e.g discarded card name
Possible triggers: "HEAL", "DAMAGE", "BURN", "MILL", "SAC", "NODESPAWN", "PLAYED_CARD". """
async def triggerFunc(ply,enemy,data,affectedPlayer):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )

