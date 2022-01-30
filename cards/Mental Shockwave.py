#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics
import random

#Simple variables
NAME = "Mental Shockwave"
COST = 1
RARITY = 'C'
DESC = "Sacrifice a random Node. If you do, your opponent burns 3 cards."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	if len(ply.nodes) > 0:
		target = random.randint(0,len(ply.nodes)-1)
		await mechanics.sacNode(ply, enemy, target)
		await enemy.burn( 3 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

