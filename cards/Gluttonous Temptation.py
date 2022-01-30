#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Gluttonous Temptation"
COST = 4
RARITY = 'U'
DESC = "Spawn a Gluttony Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from ply.addNode( 'Gluttony' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

