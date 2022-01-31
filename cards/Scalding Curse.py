#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Scalding Curse"
COST = 6
RARITY = 'R'
DESC = "Spawn a Curse Node for your opponent."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	enemy.addNode( 'Curse' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

