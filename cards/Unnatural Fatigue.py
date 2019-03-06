#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Unnatural Fatigue"
COST = 5
RARITY = 'C'
DESC = "Permanently decrease your opponent's Energy by 1."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	enemy.energy -= 1
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

