#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Staredown"
COST = 4
RARITY = 'R'
DESC = "Spawn three Pressure Nodes."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from ply.addNode( 'Pressure' )
	yield from ply.addNode( 'Pressure' )
	yield from ply.addNode( 'Pressure' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

