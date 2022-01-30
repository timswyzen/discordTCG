#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Recycle"
COST = 4
RARITY = 'R'
DESC = "Turn all your Nodes into Generator Nodes."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	for i in range( len(ply.nodes) ):
		ply.nodes[i] = 'Generator'
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

