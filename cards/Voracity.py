#!/user/bin/env python

from cardList import addCard
import tcgpowers
import mechanics

#Simple variables
NAME = "Voracity"
COST = 1
RARITY = 'U'
DESC = "Permanently increase your hunger by 1."
TARGETS = None

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.hunger = ply.hunger + 1
	
addCard( NAME, COST, RARITY, DESC, TARGETS, playFunc )

