#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Neuron Boost"
COST = 2
RARITY = 'C'
DESC = "Spawn a Neuron Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
async def playFunc(ply, enemy, target):
	await ply.addNode( 'Neuron' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

