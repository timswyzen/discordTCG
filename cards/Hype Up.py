#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Hype Up"
COST = 10
RARITY = 'R'
DESC = "Spawn a Rapid Fire Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Rapid Fire' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

