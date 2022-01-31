#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Shady Deal"
COST = 3
RARITY = 'U'
DESC = "Choose one of your Nodes. Give it to your opponent, then destroy it."
TARGETS = "FRIENDLY_NODE"
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	nodeType = nodeList[ply.nodes[target].lower()]
	ply.energy -= nodeType.energy
	ply.nodes.remove( target )
	if len(enemy.nodes) < enemy.maxNodes:
		enemy.addNode( nodeType.name )
		await mechanics.sacNode( enemy, ply, enemy.nodes.index( nodeType.name ) )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

