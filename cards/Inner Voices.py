#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Inner Voices"
COST = 5
RARITY = 'C'
DESC = "Your opponent discards two cards at random."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await enemy.randomDiscard()
	await enemy.randomDiscard()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

