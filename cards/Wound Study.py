#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Wound Study"
COST = 2
RARITY = 'C'
DESC = "Deal 2 damage to your opponent. Draw a card."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from mechanics.damage( enemy, 2 )
	ply.drawCard()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

