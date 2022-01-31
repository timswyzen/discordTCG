#!/user/bin/env python

from cardList import addCard
import mechanics, random, os

#Simple variables
NAME = "External Knowledge"
COST = 3
RARITY = 'U'
DESC = "Add a completely random card to your hand. Heal lifeforce equal to its cost."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	cardChoices = []
	for files in os.listdir('./cards'):
		cardChoices.append(files[:-3])
	chosen = random.choice(cardChoices)
	ply.hand.append(chosen)
	await mechanics.heal( ply, mechanics.cardList[chosen.lower()].cost )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

