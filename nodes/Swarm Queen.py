#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Swarm Queen"
DESC = "At the start of your turn, deal 3 damage to your opponent for each Swarmer Node you control."
ENERGY = -4


# What happens when you play it (at the start of your turn)
async def turn_func(ply, enemy, data, affected_player):
    if affected_player == ply:
        await mechanics.damage(enemy, 3 * ply.nodes.count('Swarmer'))
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=turn_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
