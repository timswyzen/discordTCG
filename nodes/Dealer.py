#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Dealer"
DESC = "Whenever a friendly Node is destroyed, if it was a Drugged Node, spawn another one."
ENERGY = -1


# What happens when the TRIGGER is triggered
async def trigger_func(ply, enemy, data, affectedPlayer):
    if affectedPlayer == "friendly" and data.name == "Drugged":
        await ply.addNode('Drugged')
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=trigger_func,
        trigger_type="SAC"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
