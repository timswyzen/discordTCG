#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Ambush"
COST = 3
RARITY = 'U'
DESC = "Sacrifice all friendly Trap Nodes."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	for idx,node in enumerate(ply.nodes):
		if node == 'Trap':
			sacNode( ply, enemy, idx )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

