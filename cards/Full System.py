#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Full System"
COST = 4
RARITY = 'C'
DESC = "Spawn a Generator Node and a Pressure Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from ply.addNode( 'Generator' )
	yield from ply.addNode( 'Pressure' )

addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )
