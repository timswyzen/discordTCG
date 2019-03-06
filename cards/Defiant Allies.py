#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Defiant Allies"
COST = 3
RARITY = 'U'
DESC = "Spawn a Defiance Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.addNode( 'Defiance' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

