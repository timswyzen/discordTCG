#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Peer Pressure"
COST = 1
RARITY = 'C'
DESC = "If you control a Drugged Node, spawn a Drugged Node for your opponent."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	if 'Drugged' in ply.nodes:
		enemy.addNode( 'Drugged' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

