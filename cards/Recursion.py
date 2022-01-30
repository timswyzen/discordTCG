#!/user/bin/env python

from cardList import addCard
import tcgpowers
import mechanics

#Simple variables
NAME = "Recursion"
COST = 2
RARITY = 'U'
DESC = "Sacrifice your first node, and spawn another of the same kind."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	if len(ply.nodes) > 0:
		killedNode = await mechanics.sacNode( ply, enemy, 0 )
		await ply.addNode( killedNode.name )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

