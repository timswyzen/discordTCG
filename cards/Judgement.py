#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Judgement"
COST = 2
RARITY = 'U'
DESC = "Choose an enemy Node. If its energy is -3 or less, destroy it."
TARGETS = "ENEMY_NODE"
TYPE = "NodeInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	if mechanics.nodeList[enemy.nodes[target].lower()].energy <= -3:
		yield from mechanics.sacNode( enemy, ply, target )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

