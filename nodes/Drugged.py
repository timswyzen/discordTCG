#!/user/bin/env python

from cardList import addNode
import tcgpowers

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Drugged"
DESC = "When this is spawned, draw a card. When it's destroyed, lose 2 energy and discard a random card."
ENERGY = 4


# Abilities that only happens when the Node is spawned
async def play_func(ply, enemy, data, affected_player):
    await ply.drawCard()
    return


# What happens when it's sacrificed/killed
async def death_func(ply, enemy, data, affected_player):
    ply.energy -= 2
    await ply.randomDiscard()
    return


FUNC_LIST = [
    NodeFunction(
        func=death_func,
        trigger_type="LTB"
    ),
    NodeFunction(
        func=play_func,
        trigger_type="ETB"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
