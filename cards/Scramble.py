#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Scramble"
COST = 2
RARITY = 'C'
DESC = "Your opponent discards a card at random."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await enemy.randomDiscard()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

