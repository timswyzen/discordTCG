#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Under Siege"
COST = 3
RARITY = 'C'
DESC = "Spawn a Siege Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Siege' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

