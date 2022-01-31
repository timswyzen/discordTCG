#!/user/bin/env python

from cardList import addNode


# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Parasite"
DESC = "At the start of your turn, spawn a Maggot Egg Node."
ENERGY = -1


# What happens when you play it (at the start of your turn)
async def turn_func(ply, enemy, data, affected_player):
    if affected_player == ply:
        await ply.addNode('Maggot Egg')
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=turn_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
