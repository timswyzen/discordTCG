#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Madness"
DESC = "Whenever your opponent discards a card, draw a card."
ENERGY = -1


# What happens when the TRIGGER is triggered
async def trigger_func(ply, enemy, discarded, affectedPlayer):
    if affectedPlayer == "enemy":
        await ply.drawCard()
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=trigger_func,
        trigger_type="DISCARD"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
