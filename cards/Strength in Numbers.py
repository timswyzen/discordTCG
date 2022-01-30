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
def playFunc(ply, enemy, target):
	yield from ply.addNode( "Prayer" )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

