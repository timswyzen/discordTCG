#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Hivemind"
COST = 5
RARITY = 'C'
DESC = "If you control a Swarmer Node, spawn two Swarmer Nodes."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	if 'Swarmer' in ply.nodes:
		await ply.addNode( 'Swarmer' )
		await ply.addNode( 'Swarmer' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

