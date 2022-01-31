#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Genetic Analysis"
COST = 5
RARITY = 'C'
DESC = "Spawn a copy of one of your Nodes."
TARGETS = "FRIENDLY_NODE"
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( ply.nodes[target] )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

