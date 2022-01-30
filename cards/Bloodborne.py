#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Bloodborne"
COST = 7
RARITY = 'R'
DESC = "Spawn a Blood Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from ply.addNode( 'Blood' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

