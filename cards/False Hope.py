#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "False Hope"
COST = 3
RARITY = 'C'
DESC = "Double your opponent's Desperation until end of turn."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	enemy.desperationBoost += enemy.desperation
	enemy.desperation += enemy.desperation
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

