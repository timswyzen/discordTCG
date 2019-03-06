#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Confusion"
COST = 4
RARITY = 'U'
DESC = "Target player swaps their Hunger and Desperation stats."
TARGETS = "PLAYER"
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	if target == 1:
		ply.desperation, ply.hunger = ply.hunger, ply.desperation
	elif target == 2:
		enemy.desperation, enemy.hunger = enemy.hunger, enemy.desperation
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

