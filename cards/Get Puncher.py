#!/user/bin/env python

from cardList import addCard
import tcgpowers

#Simple variables
NAME = "Get Puncher"
COST = 1
RARITY = 'C'
DESC = "Spawns a Puncher node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.addNode( 'Puncher' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

