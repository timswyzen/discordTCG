#!/user/bin/env python

from cardList import addCard
import tcgpowers

#Simple variables
NAME = "Swing"
COST = 1
RARITY = 'C'
DESC = "Deal 2 damage to your opponent."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	enemy.lifeforce = enemy.lifeforce - 2
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

