#!/user/bin/env python

from cardList import addCard


#Simple variables
NAME = "Embrace Temptation"
COST = 0
RARITY = 'R'
DESC = "Spawns a Tempter node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Tempter' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

