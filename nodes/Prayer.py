#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Prayer"
DESC = "At the start of your turn, heal 1 lifeforce for each Node you control."
ENERGY = -2


# What happens when you play it
async def turn_func(ply, enemy, data, affected_player):
    if affected_player == ply:
        await mechanics.heal(ply, len(ply.nodes))
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=turn_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
