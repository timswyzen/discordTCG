#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Leveled Field"
COST = 15
RARITY = 'R'
DESC = "Reset both players' lifeforces to the starting amount."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	ply.lifeforce = 35
	enemy.lifeforce = 35
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

