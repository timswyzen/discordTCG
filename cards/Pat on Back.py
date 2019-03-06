#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Pat on Back"
COST = 5
RARITY = 'C'
DESC = "Permanently increase your Energy by 1."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.energy += 1
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

