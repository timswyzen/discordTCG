#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Fizzle"
COST = 2
RARITY = 'C'
DESC = "Gain 1 Hunger and 1 Desperation. Draw a card."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	ply.hunger += 1
	ply.desperation += 1
	await ply.drawCard()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

