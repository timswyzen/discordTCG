#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Static Interference"
COST = 4
RARITY = 'C'
DESC = "Spawn a Scrambler Trap."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Scrambler Trap' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

