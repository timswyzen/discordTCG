#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Swing"
COST = 1
RARITY = 'C'
DESC = "Deal 2 damage to your opponent."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from mechanics.damage( enemy, 2 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

