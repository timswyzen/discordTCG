#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Innocence"
COST = 4
RARITY = 'C'
DESC = "Spawn a Lifeflame Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from ply.addNode( 'Lifeflame' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

