#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Strength in Numbers"
COST = 3
RARITY = 'R'
DESC = "Spawn a Prayer Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( "Prayer" )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

