#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Tripwire"
COST = 2
RARITY = 'C'
DESC = "Spawn a Trap Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Trap' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

