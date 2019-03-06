#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics, random

#Simple variables
NAME = "Feral Reach"
COST = 3
RARITY = 'U'
DESC = "If you have at least 15 Desperation, spawn a random Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	if ply.desperation >= 15:
		nodeChoices = []
		for files in os.listdir('./nodes'):
			nodeChoices.append(files[:-3])
		ply.addNode( random.choice( nodeChoices ) )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

