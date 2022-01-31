#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Fountain"
DESC = "When this Node spawns or is destroyed, draw a card."
ENERGY = 0


# Abilities that only happens when the Node is spawned
async def enter_func(ply, enemy):
    await ply.drawCard()
    return


# What happens when it's sacrificed/killed
async def death_func(ply, enemy):
    await ply.drawCard()
    return


FUNC_LIST = [
    NodeFunction(
        func=enter_func,
        trigger_type="ETB"
    ),
    NodeFunction(
        func=death_func,
        trigger_type="LTB"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
