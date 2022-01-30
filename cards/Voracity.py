#!/user/bin/env python

from cardList import addCard
import tcgpowers
import mechanics

#Simple variables
NAME = "Voracity"
COST = 2
RARITY = 'C'
DESC = "Permanently increase your Hunger by 5."
TARGETS = None
TYPE = "Buff"

#What happens when you play it
async def playFunc(ply, enemy, target):
	ply.hunger += 5
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

