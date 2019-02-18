#!/user/bin/env python

from cardList import addCard
import tcgpowers

#Simple variables
NAME = "Minor Panic"
COST = 2
RARITY = 'C'
DESC = "Permanently increase your desperation by 1."
TARGETS = None

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.desperation = ply.desperation + 1
	
addCard( NAME, COST, RARITY, DESC, TARGETS, playFunc )

