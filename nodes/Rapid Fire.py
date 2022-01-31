#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Rapid Fire"
DESC = "Whenever you play a card that doesn't spawn a Node, you can spawn another Node this turn."
ENERGY = -5


async def trigger_func(ply, enemy, data, affectedPlayer):
    if affectedPlayer == "self" and not mechanics.cardList[data.lower()].cardtype == "NodeGen":
        ply.playedNode = False  # don't need to check for nodegen cause it'll just overwrite this anyway... better than redoing data arg
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=trigger_func,
        trigger_type="PLAYED_CARD"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
