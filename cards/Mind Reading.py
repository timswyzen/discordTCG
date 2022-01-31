#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Mind Reading"
COST = 5
RARITY = 'R'
DESC = "If you have the same exact hand as your opponent (besides this card), your opponent's lifeforce becomes 1."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	handSame = True
	for plyCards in ply.hand:
		if plyCards not in enemy.hand:
			handSame = False
			break
	for enemyCards in enemy.hand:
		if enemyCards not in ply.hand:
			handSame = False
			break
	if handSame == True:
		enemy.lifeforce = 1
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

