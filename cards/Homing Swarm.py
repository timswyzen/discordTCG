#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Homing Swarm"
COST = 6
RARITY = 'U'
DESC = "Spawn a Swarmer Node. If your opponent milled last turn, spawn two Swarmer Nodes instead."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Swarmer' )
	if enemy.milled == True:
		await ply.addNode( 'Swarmer' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

