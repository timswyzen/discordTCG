#!/user/bin/env python

from cardList import addCard
import tcgpowers

#Simple variables
NAME = "Embrace Temptation"
COST = 0
RARITY = 'R'
DESC = "Gives you a Tempter node."
TARGETS = None

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.addNode( 'Tempter', -3 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, playFunc )

