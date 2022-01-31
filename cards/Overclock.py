#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Overclock"
COST = 9
RARITY = 'U'
DESC = "Destroy all friendly Generator Nodes and permanently gain 2 energy for each destroyed."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	amtToGain = 0
	tempNodes = ply.nodes.copy()[::-1]
	for idx,node in enumerate(tempNodes):
		if 'Generator' in node: 
			amtToGain += 2
			await mechanics.sacNode( ply, enemy, len(tempNodes)-1-idx )
	ply.energy += amtToGain
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

