#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Selfish Sacrifice"
COST = 3
RARITY = 'C'
DESC = "Sacrifice a friendly Node. If you do, heal 8 lifeforce."
TARGETS = "FRIENDLY_NODE"
TYPE = "NodeInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	if len(ply.nodes) > 0:
		yield from mechanics.sacNode( ply, enemy, target )
		yield from mechanics.heal( ply, 8 )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

