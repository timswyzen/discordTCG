#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Caltrops"
COST = 6
RARITY = 'R'
DESC = "Spawn 3 Trap Nodes."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.addNode( 'Trap' )
	ply.addNode( 'Trap' )
	ply.addNode( 'Trap' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

