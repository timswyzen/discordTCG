#!/user/bin/env python

from cardList import addCard
import mechanics, random

#Simple variables
NAME = "Memory Lapse"
COST = 6
RARITY = 'C'
DESC = "Your opponent puts a random card from their hand on top of their deck."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	discarded = enemy.hand.pop( random.randint(0,len(enemy.hand)-1) )
	enemy.deck.append( discarded )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

