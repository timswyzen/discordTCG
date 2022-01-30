#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Queen's Grace"
COST = 4
RARITY = 'R'
DESC = "If you control at least two Swarmer Nodes, sacrifice two Swarmer Nodes and spawn a Swarm Queen Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	if ply.nodes.count( 'Swarmer' ) >= 2:
		yield from mechanics.sacNode( ply, enemy, ply.nodes.index( 'Swarmer' ) )
		yield from mechanics.sacNode( ply, enemy, ply.nodes.index( 'Swarmer' ) )
		yield from ply.addNode( 'Swarm Queen' )
	
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

