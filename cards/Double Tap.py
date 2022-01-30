#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Double Tap"
COST = 6
RARITY = 'C'
DESC = "Destroy an enemy Node, then deal 2 damage to its owner."
TARGETS = "ENEMY_NODE"
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await mechanics.sacNode( enemy, ply, target )
	await mechanics.damage( enemy, 2 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

