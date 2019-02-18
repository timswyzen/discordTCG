#!/user/bin/env python

from cardList import addNode
import tcgpowers

#Simple variables
NAME = "Puncher"
DESC = "Deals 1 damage to your opponent each turn."
ENERGY = -1

#What happens when you play it
def playFunc(ply,enemy):
	print( "Dealt 1 damage to " + enemy.name )
	enemy.lifeforce = enemy.lifeforce - 1
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, ENERGY, deathFunc )

