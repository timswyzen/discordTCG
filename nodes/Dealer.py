#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

# Simple variables
NAME = "Dealer"
DESC = "Whenever a friendly Node is destroyed, if it was a Drugged Node, spawn another one."
ENERGY = -1
TRIGGER = "SAC"


# What happens when you play it (at the start of your turn)
async def playFunc(ply, enemy):
    return


# Abilities that only happens when the Node is spawned
async def oneTimeFunc(ply, enemy):
    return


# What happens when it's sacrificed/killed
async def deathFunc(ply, enemy):
    return


# What happens when the TRIGGER is triggered
async def triggerFunc(ply, enemy, data, affectedPlayer):
    if affectedPlayer == "friendly" and data.name == "Drugged":
        await ply.addNode('Drugged')
    else:
        return False


addNode(NAME, DESC, playFunc, oneTimeFunc, ENERGY, deathFunc, TRIGGER, triggerFunc)
