#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Inherited Cruelty"
COST = 3
RARITY = 'U'
DESC = "For each other card you've played this turn up to 4, spawn a Swarmer Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	i = 0
	for _ in range( ply.cardsThisTurn ):
		if i < 3:
			await ply.addNode( 'Swarmer' )
		i += 1
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

