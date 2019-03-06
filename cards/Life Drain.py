#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Life Drain"
COST = 4
RARITY = 'C'
DESC = "Deal 7 damage to your opponent. Heal 7 lifeforce."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from mechanics.heal( ply, 7 )
	yield from mechanics.damage( enemy, 7 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

