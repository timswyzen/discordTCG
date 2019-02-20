#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Lesser Leech"
DESC = "At the end of your turn, deal 2 damage to your opponent. Gain lifeforce equal to the damage dealt."
ENERGY = -1

#What happens when you play it
def playFunc(ply,enemy):
	enemy.lifeforce = enemy.lifeforce - 2
	ply.lifeforce = ply.lifeforce + 2
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

