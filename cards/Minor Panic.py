#!/user/bin/env python

from cardList import addCard


#Simple variables
NAME = "Minor Panic"
COST = 2
RARITY = 'C'
DESC = "Permanently increase your Desperation by 5."
TARGETS = None
TYPE = "Buff"

#What happens when you play it
async def playFunc(ply, enemy, target):
	ply.desperation += 5
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

