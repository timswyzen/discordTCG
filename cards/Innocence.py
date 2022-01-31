#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Innocence"
COST = 4
RARITY = 'C'
DESC = "Spawn a Lifeflame Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Lifeflame' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

