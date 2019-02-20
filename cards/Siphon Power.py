#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics
import math

#Simple variables
NAME = "Siphon Power"
COST = 4
RARITY = 'C'
DESC = "Draw a card for every 2 Nodes you control."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	for _ in range( math.floor(len(ply.nodes)/2) ):
		ply.drawCard()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

