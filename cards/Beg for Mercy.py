#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Beg for Mercy"
COST = 1
RARITY = 'C'
DESC = "Heal 5 lifeforce."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await mechanics.heal( ply, 5 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

