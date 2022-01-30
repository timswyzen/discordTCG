#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Pleasant Memories"
COST = 5
RARITY = 'U'
DESC = "Spawn a Nostalgia Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from ply.addNode( 'Nostalgia' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

