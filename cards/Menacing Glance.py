#!/user/bin/env python

from cardList import addCard
import tcgpowers

#Simple variables
NAME = "Menacing Glance"
COST = 1
RARITY = 'C'
DESC = "Spawns a Pressure node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.addNode( 'Pressure' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

