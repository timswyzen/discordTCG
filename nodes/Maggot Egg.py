#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Maggot Egg"
DESC = "At the start of your turn, sacrifice this Node and spawn a Parasite Node."
ENERGY = 0

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	sacNode( ply, enemy, ply.nodes.index( 'Maggot Egg' ) )
	ply.addNode( 'Parasite' )
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

