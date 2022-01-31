#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Queen's Grace"
COST = 4
RARITY = 'R'
DESC = "If you control at least two Swarmer Nodes, sacrifice two Swarmer Nodes and spawn a Swarm Queen Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	if ply.nodes.count( 'Swarmer' ) >= 2:
		await mechanics.sacNode( ply, enemy, ply.nodes.index( 'Swarmer' ) )
		await mechanics.sacNode( ply, enemy, ply.nodes.index( 'Swarmer' ) )
		await ply.addNode( 'Swarm Queen' )
	
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

