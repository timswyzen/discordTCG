#!/user/bin/env python

from cardList import addNode


# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Curse"
DESC = "At the start of your turn, burn 4 cards."
ENERGY = 0


# What happens when you play it (at the start of your turn)
async def burn_func(ply, enemy, data, affected_player):
    if affected_player == "self":
        await ply.burn(4)
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=burn_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
