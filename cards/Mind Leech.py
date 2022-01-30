#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Mind Leech"
COST = 4
RARITY = 'C'
DESC = "Draw two cards. If your opponent milled last turn, draw an additional card."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.drawCard()
	await ply.drawCard()
	if enemy.milled == True:
		await ply.drawCard()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

