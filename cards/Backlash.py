#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Backlash"
COST = 4
RARITY = 'C'
DESC = "Deal 2 damage to your opponent for each Node he or she controls."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await mechanics.damage( enemy, 2*len(enemy.nodes) )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

