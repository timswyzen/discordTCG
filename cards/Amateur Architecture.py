#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Amateur Architecture"
COST = 4
RARITY = 'R'
DESC = "Draw five cards. Spawn a Foundation Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	for _ in range( 5 ):
		yield from ply.drawCard()
	yield from ply.addNode( 'Foundation' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

