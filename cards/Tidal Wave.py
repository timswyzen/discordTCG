#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Tidal Wave"
COST = 18
RARITY = 'C'
DESC = "Destroy all enemy Nodes."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	for _ in range( len(enemy.nodes) ):
		yield from mechanics.sacNode( enemy, ply, 0 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

