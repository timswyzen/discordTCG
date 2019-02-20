#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Demonic Trap"
DESC = "When this Node is destroyed, destroy an opponent's Node at random."
ENERGY = -1

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	target = random.randint(0,len(enemy.nodes))
	mechanics.sacNode(enemy, ply, target)
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

