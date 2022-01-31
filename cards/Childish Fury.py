#!/user/bin/env python

from cardList import addCard
import mechanics

#Simple variables
NAME = "Childish Fury"
COST = 4
RARITY = 'C'
DESC = "Add 5 Slap cards to your deck, then shuffle it."
TARGETS = None
TYPE = "DeckInteraction"

#What happens when you play it
async def playFunc(ply, enemy, target):
	for _ in range( 5 ):
		ply.deck.append( 'Slap' )
	ply.shuffle()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

