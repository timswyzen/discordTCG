#!/user/bin/env python

from cardList import addCard
import tcgpowers

#Simple variables
NAME = "Get Puncher"
COST = 1
RARITY = 'C'
DESC = "Gives you a Puncher node."
TARGETS = None

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.addNode( 'Puncher', -1 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, playFunc )

