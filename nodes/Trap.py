#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Trap"
DESC = "When destroyed, deal 3 damage to your opponent."
ENERGY = 0

#What happens when you play it
def playFunc(ply,enemy):
	return
	
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	enemy.lifeforce = enemy.lifeforce - 3
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

