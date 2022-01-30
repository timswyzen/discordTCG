#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Bloody Pentagram"
COST = 2
RARITY = 'C'
DESC = "Spawn a Demonic Trap Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Demonic Trap' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

