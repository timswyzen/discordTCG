#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Hasty Shot"
COST = 4
RARITY = 'C'
DESC = "Destroy an enemy Node. Your opponent heals for 6."
TARGETS = "ENEMY_NODE"
TYPE = "NodeInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from mechanics.sacNode(enemy,ply,target)
	yield from mechanics.heal( enemy, 6 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

