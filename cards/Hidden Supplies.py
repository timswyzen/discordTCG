#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Hidden Supplies"
COST = 2
RARITY = 'C'
DESC = "Spawn a Supplies Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Supplies' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

