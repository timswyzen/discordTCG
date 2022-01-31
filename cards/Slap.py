#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Slap"
COST = 1
RARITY = 'S'
DESC = "Deal 1 damage to your opponent."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await mechanics.damage( enemy, 1 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

