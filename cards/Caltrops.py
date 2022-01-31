#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Caltrops"
COST = 6
RARITY = 'R'
DESC = "Spawn 3 Trap Nodes."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Trap' )
	await ply.addNode( 'Trap' )
	await ply.addNode( 'Trap' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

