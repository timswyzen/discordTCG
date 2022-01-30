#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Foundation"
DESC = "When this is destroyed, sacrifice all your other Nodes."
ENERGY = 1
TRIGGER = None

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	for i in range( len(ply.nodes) ):
		if not ply.nodes[i] == 'Foundation':
			yield from mechanics.sacNode( ply, enemy, 0 )
	return
	
#What happens when the TRIGGER is triggered
def triggerFunc(ply,enemy):
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )

