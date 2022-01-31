#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Energy Blast"
COST = 4
RARITY = 'R'
DESC = "Deal damage to your opponent equal to your total energy (counts negative numbers)."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await mechanics.damage( enemy, ply.energy )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

