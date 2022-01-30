#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Ostracize"
COST = 3
RARITY = 'C'
DESC = "Heal lifeforce equal to your opponent's Desperation."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await mechanics.heal( ply, enemy.desperation )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

