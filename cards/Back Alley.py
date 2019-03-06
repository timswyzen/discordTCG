#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Back Alley"
COST = 4
RARITY = 'U'
DESC = "Spawn a Dealer Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.addNode( 'Dealer' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

