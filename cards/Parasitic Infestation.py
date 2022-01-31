#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Parasitic Infestation"
COST = 9
RARITY = 'R'
DESC = "Spawn a Parasite Node for your opponent."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	enemy.addNode( 'Parasite' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

