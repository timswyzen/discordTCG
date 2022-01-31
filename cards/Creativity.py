#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Creativity"
COST = 4
RARITY = 'C'
DESC = "You can spawn a Node again this turn after playing this card."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	ply.playedNode = False
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

