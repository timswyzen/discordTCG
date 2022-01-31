#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Siege"
DESC = "At the start of your turn, increase your opponent's Desperation and Hunger by 5."
ENERGY = 2


# What happens when you play it (at the start of your turn)
async def turn_func(ply, enemy, data, affected_player):
    if affected_player == ply:
        enemy.hunger += 5
        enemy.desperation += 5
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=turn_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
