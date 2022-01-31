#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Collected Shot"
COST = 4
RARITY = 'U'
DESC = "If you control at least four Nodes, deal 10 damage to your opponent."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	if len(ply.nodes) >= 4:
		await mechanics.damage( enemy, 10 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

