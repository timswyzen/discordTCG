#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Drug Infusion"
COST = 3
RARITY = 'C'
DESC = "Spawn two Generator Nodes."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from ply.addNode( 'Generator' )
	yield from ply.addNode( 'Generator' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

