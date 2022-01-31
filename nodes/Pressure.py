#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Pressure"
DESC = "At the start of your turn, deal 1 damage to your opponent."
ENERGY = -1


# What happens when you play it
async def play_func(ply, enemy, data, affected_player):
    if affected_player == ply:
        await mechanics.damage(enemy, 1)
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=play_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
