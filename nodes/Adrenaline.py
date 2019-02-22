#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Adrenaline"
DESC = "At the start of your turn, if you have less than 15 lifeforce, sacrifice this Node and gain 5 lifeforce and 5 Desperation."
ENERGY = -1

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	if ply.lifeforce < 15:
		ply.lifeforce += 5
		ply.desperation += 5
		mechanics.sacNode( ply, enemy, ply.nodes.index('Adrenaline') )
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

