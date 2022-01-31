#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Swarmer"
DESC = "At the start of your turn, deal 1 damage to your opponent for each Swarmer you control."
ENERGY = -3


# What happens when you play it (at the start of your turn)
async def turn_func(ply, enemy, data, affected_player):
    if affected_player == ply:
        await mechanics.damage(enemy, ply.nodes.count('Swarmer'))
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=turn_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
