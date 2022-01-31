#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Ray of Hope"
COST = 4
RARITY = 'U'
DESC = "Spawn a Hope Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Hope' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

