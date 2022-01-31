#!/user/bin/env python

from cardList import addNode
import tcgpowers

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Reason"
DESC = "You can't mill cards."
ENERGY = -1


# What happens when you play it (at the start of your turn)
async def turn_func(ply, enemy, data, affected_player):
    # TODO: test
    ply.milled = True
    return False


FUNC_LIST = [
    NodeFunction(
        func=turn_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
