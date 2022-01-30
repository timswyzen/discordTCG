#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Prolong the Inevitable"
COST = 6
RARITY = 'U'
DESC = "Heal 18 lifeforce. Spawn a Lesser Leech Node for your opponent."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await mechanics.heal( ply, 18 )
	enemy.addNode( 'Lesser Leech' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

