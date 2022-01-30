#!/user/bin/env python

from cardList import addCard
import tcgpowers

#Simple variables
NAME = "Embrace Temptation"
COST = 0
RARITY = 'R'
DESC = "Spawns a Tempter node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from ply.addNode( 'Tempter' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

