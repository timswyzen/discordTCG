#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Life Drain"
COST = 4
RARITY = 'C'
DESC = "Deal 7 damage to your opponent. Heal 7 lifeforce."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await mechanics.heal( ply, 7 )
	await mechanics.damage( enemy, 7 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

