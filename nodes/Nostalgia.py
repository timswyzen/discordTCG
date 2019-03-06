#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

#Simple variables
NAME = "Nostalgia"
DESC = "Whenever you play a card, you heal for 1."
ENERGY = -1
TRIGGER = "PLAYED_CARD"

#What happens when you play it (at the start of your turn)
def playFunc(ply,enemy):
	return
	
#Abilities that only happens when the Node is spawned
def oneTimeFunc(ply,enemy):
	return
	
#What happens when it's sacrificed/killed
def deathFunc(ply,enemy):
	return
	
"""What happens when the TRIGGER is triggered. 
If it was triggered by owner, affectedPlayer is "friendly"
If it was triggered by the enemy, affectedPlayer is "enemy"
data is whatever data is relevant to the trigger, e.g discarded card name
Possible triggers: "HEAL", "DAMAGE", "BURN", "MILL", "SAC", "NODESPAWN", "PLAYED_CARD". """
def triggerFunc(ply,enemy,data,affectedPlayer):
	print('before check')
	if affectedPlayer == "friendly":
		print('after check')
		yield from mechanics.heal( ply, 1 )
		print('after heal')
	return
	
addNode( NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc )

