#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Remove Expendables"
COST = 8
RARITY = 'U'
DESC = "Clear your hand. Draw six cards."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	ply.hand = []
	for _ in range( 6 ):
		await ply.drawCard()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

