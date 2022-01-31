#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Strangle"
COST = 4
RARITY = 'U'
DESC = "Spawn a Net Trap Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Net Trap' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

