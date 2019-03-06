#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Mental Chokehold"
COST = 6
RARITY = 'C'
DESC = "Your opponent can't gain Nodes until your next turn."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.opponentCantSpawnNodes = True
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

