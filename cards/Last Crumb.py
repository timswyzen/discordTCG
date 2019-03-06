#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Last Crumb"
COST = 3
RARITY = 'C'
DESC = "Add 10 Hunger to the player with the lowest Desperation. Add it to yourself if they're equal."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	if ply.desperation > enemy.desperation:
		enemy.hunger += 10
	else:
		ply.hunger += 10
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

