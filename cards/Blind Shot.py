#!/user/bin/env python

from cardList import addCard
import mechanics, random

#Simple variables
NAME = "Blind Shot"
COST = 2
RARITY = 'C'
DESC = "Destroy a random enemy Node."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	if len(enemy.nodes) > 0:
		await mechanics.sacNode( enemy, ply, random.randint( 0, len(enemy.nodes)-1 ) )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

