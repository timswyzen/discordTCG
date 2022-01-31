#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Force Feed"
COST = 2
RARITY = 'C'
DESC = "Decrease your opponent's Hunger by 5."
TARGETS = None
TYPE = "Debuff"

#What happens when you play it
async def playFunc(ply, enemy, target):
	enemy.hunger -= 5
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

