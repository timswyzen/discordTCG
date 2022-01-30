#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Desperate Measures"
COST = 3
RARITY = 'C'
DESC = "Spawn a Drugged Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from ply.addNode( 'Drugged' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

