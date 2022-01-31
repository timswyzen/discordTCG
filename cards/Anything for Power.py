#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Anything for Power"
COST = 1
RARITY = 'U'
DESC = "Choose and sacrifice a friendly Node. If you do, draw a card."
TARGETS = "FRIENDLY_NODE"
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	if len(ply.nodes) > 0:
		await mechanics.sacNode( ply, enemy, target )
		await ply.drawCard()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

