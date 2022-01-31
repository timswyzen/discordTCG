#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Spark"
COST = 9
RARITY = 'C'
DESC = "Spawn two Electricity Nodes."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Electricity' )
	await ply.addNode( 'Electricity' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

