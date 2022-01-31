#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Deep Breath"
COST = 1
RARITY = 'C'
DESC = "Heal 10 lifeforce. Lose 5 Desperation."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	ply.desperation -= 5
	await mechanics.heal( ply, 10 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

