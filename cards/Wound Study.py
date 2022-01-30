#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Wound Study"
COST = 2
RARITY = 'C'
DESC = "Deal 2 damage to your opponent. Draw a card."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await mechanics.damage( enemy, 2 )
	await ply.drawCard()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

