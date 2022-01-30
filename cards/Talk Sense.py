#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Talk Sense"
COST = 7
RARITY = 'C'
DESC = "Spawn a Reason Node for your opponent."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	enemy.addNode( 'Reason' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

