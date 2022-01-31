#!/user/bin/env python

from cardList import addNode


# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Gluttony"
DESC = "At the start of your turn, decrease your opponent's Hunger by 10."
ENERGY = -4


# What happens when you play it (at the start of your turn)
async def turn_func(ply, enemy, data, affected_player):
    if affected_player == ply:
        enemy.hunger -= 10
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=turn_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
