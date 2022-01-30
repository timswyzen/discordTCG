#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Grand Feast"
COST = 5
RARITY = 'R'
DESC = "Spawn a Feast Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from ply.addNode( 'Feast' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

