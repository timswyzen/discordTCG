#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Maul"
COST = 2
RARITY = 'C'
DESC = "Deal 5 damage to your opponent."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from mechanics.damage( enemy, 5 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

