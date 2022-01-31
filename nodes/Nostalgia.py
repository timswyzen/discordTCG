#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Nostalgia"
DESC = "Whenever you play a card, you heal for 1."
ENERGY = -1


async def trigger_func(ply, enemy, data, affectedPlayer):
    if affectedPlayer == "friendly":
        await mechanics.heal(ply, 1)
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=trigger_func,
        trigger_type="PLAYED_CARD"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
