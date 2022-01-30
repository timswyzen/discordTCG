#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

# Simple variables
NAME = "Mind Swap"
COST = 6
RARITY = 'U'
DESC = "Swap Desperation and Hunger with your opponent until your next turn."
TARGETS = None
TYPE = "PlyInteraction"


# What happens when you play it
async def playFunc(ply, enemy, target):
    ply.mindSwap = True  # for the playerbase thing TODO: find a better way lol
    ply.desperation, enemy.desperation = enemy.desperation, ply.desperation
    ply.hunger, enemy.hunger = enemy.hunger, ply.hunger


addCard(NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc)
