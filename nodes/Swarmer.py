#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Swarmer"
DESC = "At the start of your turn, deal 1 damage to your opponent for each Swarmer you control."
ENERGY = -2

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	enemy.lifeforce -= ply.nodes.count('Swarmer')
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

