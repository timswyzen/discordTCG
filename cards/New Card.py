#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = ""
COST = 2
RARITY = 'C'
DESC = ""
TARGETS = ""
TYPE = ""

#What happens when you play it
def playFunc(ply, enemy, target):
	
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

