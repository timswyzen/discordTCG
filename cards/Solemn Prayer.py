#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Solemn Prayer"
COST = 3
RARITY = 'C'
DESC = "Permanently decrease your opponent's Desperation by 10."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	enemy.desperation -= 10
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

