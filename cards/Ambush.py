#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Ambush"
COST = 3
RARITY = 'U'
DESC = "Sacrifice all friendly Trap-type Nodes."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	tempNodes = ply.nodes.copy()[::-1]
	for idx,node in enumerate(tempNodes):
		if 'Trap' in node: 
			await mechanics.sacNode( ply, enemy, len(tempNodes)-1-idx )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

