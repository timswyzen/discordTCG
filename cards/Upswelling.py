#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Upswelling"
COST = 3
RARITY = 'U'
DESC = "Spawn a Fountain Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Fountain' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

