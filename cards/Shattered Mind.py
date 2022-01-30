#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Shattered Mind"
COST = 5
RARITY = 'R'
DESC = "If your opponent has at least 35 Desperation, deal damage to them equal to half their health total, rounded up."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	if enemy.desperation >= 35:
		enemy.lifeforce = round(enemy.lifeforce - enemy.lifeforce/2)
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

