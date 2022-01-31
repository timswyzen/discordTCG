#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Minor Recharge"
COST = 1
RARITY = 'C'
DESC = "Spawn a Generator Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Generator' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

