#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics, math

#Simple variables
NAME = "Unnoble Sacrifice"
COST = 13
RARITY = 'R'
DESC = "Lose half your lifeforce, rounded up. Your opponent burns that many cards."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	lifeLost = math.ceil( ply.lifeforce / 2 )
	yield from mechanics.damage( ply, lifeLost )
	yield from enemy.burn( lifeLost )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

