#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Change of Plans"
COST = 2
RARITY = 'U'
DESC = "Sacrifice a friendly Node. If you do, spawn two Generator Nodes."
TARGETS = "FRIENDLY_NODE"
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	mechanics.sacNode( ply, enemy, target )
	ply.addNode( 'Generator' )
	ply.addNode( 'Generator' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

