#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Shell Shock"
COST = 1
RARITY = 'C'
DESC = "Increase your opponent's Desperation by 5."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	enemy.desperation += 5
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

