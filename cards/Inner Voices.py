#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Inner Voices"
COST = 5
RARITY = 'C'
DESC = "Your opponent discards two cards at random."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from enemy.randomDiscard()
	yield from enemy.randomDiscard()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

