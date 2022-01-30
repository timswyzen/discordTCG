#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Static Interference"
COST = 4
RARITY = 'C'
DESC = "Spawn a Scrambler Trap."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from ply.addNode( 'Scrambler Trap' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

