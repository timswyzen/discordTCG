#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Hellfire"
COST = 4
RARITY = 'U'
DESC = "Both players burn 8 cards."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.burn(8)
	await enemy.burn(8)
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

