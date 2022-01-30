#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Cataclysm"
COST = 10
RARITY = 'R'
DESC = "Destroy all Nodes."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	for _ in range( len(enemy.nodes) ):
		await mechanics.sacNode( enemy, ply, 0 )
	for _ in range( len(ply.nodes) ):
		await mechanics.sacNode( ply, enemy, 0 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

