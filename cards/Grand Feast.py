#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Grand Feast"
COST = 5
RARITY = 'R'
DESC = "Spawn a Feast Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Feast' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

