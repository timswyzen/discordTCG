#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Staredown"
COST = 4
RARITY = 'R'
DESC = "Spawn three Pressure Nodes."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Pressure' )
	await ply.addNode( 'Pressure' )
	await ply.addNode( 'Pressure' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

