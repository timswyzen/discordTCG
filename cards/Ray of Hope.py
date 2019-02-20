#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Ray of Hope"
COST = 4
RARITY = 'U'
DESC = "Spawn a Hope Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.addNode( 'Hope' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

