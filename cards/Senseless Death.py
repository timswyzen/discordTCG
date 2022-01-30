#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Senseless Death"
COST = 0
RARITY = 'C'
DESC = "Sacrifice one of your Nodes."
TARGETS = "FRIENDLY_NODE"
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await mechanics.sacNode( ply, enemy, target )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

