#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Killer's Aura"
COST = 4
RARITY = 'U'
DESC = "Your opponent burns a card for each Node you control."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await enemy.burn( len(ply.nodes) )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

