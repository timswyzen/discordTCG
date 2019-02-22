#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Pressure"
DESC = "At the start of your turn, deal 1 damage to your opponent."
ENERGY = -1

#What happens when you play it
def playFunc(ply,enemy):
	enemy.lifeforce -= 1
	
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc )

