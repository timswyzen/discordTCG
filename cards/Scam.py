#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Scam"
COST = 4
RARITY = 'U'
DESC = "Steal one of your opponent's Nodes."
TARGETS = "ENEMY_NODE"
TYPE = "NodeInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	if len(enemy.nodes) > 0:
		target = random.randint( 0, len(enemy.nodes)-1 )
		nodeType = mechanics.nodeList[enemy.nodes[target].lower()]
		ply.addNode( enemy.nodes[target] )
		enemy.energy -= nodeType.energy
		enemy.nodes.pop( target )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

