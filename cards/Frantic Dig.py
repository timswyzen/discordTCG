#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Frantic Dig"
COST = 2
RARITY = 'C'
DESC = "You can mill again this turn after playing this card."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	ply.milled = False
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

