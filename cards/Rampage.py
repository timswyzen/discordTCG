#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Rampage"
COST = 1
RARITY = 'U'
DESC = "Destroy a random Node for each player."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	if len(enemy.nodes) > 0:
		mechanics.sacNode( enemy, ply, random.randint( 0, len(enemy.nodes)-1 ) )
	if len(ply.nodes) > 0:
		mechanics.sacNode( ply, enemy, random.randint( 0, len(ply.nodes)-1 ) )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

