#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Spark"
COST = 9
RARITY = 'C'
DESC = "Spawn two Electricity Nodes."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from ply.addNode( 'Electricity' )
	yield from ply.addNode( 'Electricity' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

