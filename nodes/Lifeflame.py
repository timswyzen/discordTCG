#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Lifeflame"
DESC = "At the start of your turn, burn 4 cards."
ENERGY = 3


# What happens when you play it (at the start of your turn)
async def turn_func(ply, enemy, data, affected_player):
    if affected_player == ply:
        await ply.burn(4)
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=turn_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
