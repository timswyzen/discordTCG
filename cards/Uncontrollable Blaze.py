#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Uncontrollable Blaze"
COST = 2
RARITY = 'U'
DESC = "Destroy all Nodes. Lose 3 lifeforce for each Node destroyed."
TARGETS = None
TYPE = "NodeInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	selfDmg = 0
	for _ in range( len(enemy.nodes) ):
		yield from mechanics.sacNode( enemy, ply, 0 )
		selfDmg += 3
	for _ in range( len(ply.nodes) ):
		yield from mechanics.sacNode( ply, enemy, 0 )
		selfDmg += 3
	yield from mechanics.damage( ply, selfDmg )
	
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

