#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Inhumane Experimentation"
COST = 2
RARITY = 'C'
DESC = "Choose one of your Nodes and activate its death ability without destroying it."
TARGETS = "FRIENDLY_NODE"
TYPE = "NodeInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	nodeObj = mechanics.nodeList[ ply.nodes[target].lower() ]
	nodeObj.deathFunc( ply, enemy )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

