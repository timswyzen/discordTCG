#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Refocus"
COST = 4
RARITY = 'C'
DESC = "Increase your Hunger and Desperation by 3. Draw a card."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.hunger += 3
	ply.desperation += 3
	ply.drawCard()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

