#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Tidal Wave"
COST = 18
RARITY = 'C'
DESC = "Destroy all enemy Nodes."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	for _ in range( len(enemy.nodes) ):
		await mechanics.sacNode( enemy, ply, 0 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

