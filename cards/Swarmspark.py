#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Swarmspark"
COST = 1
RARITY = 'C'
DESC = "Spawn a Swarmer Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.addNode( 'Swarmer' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

