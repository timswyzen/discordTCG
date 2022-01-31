#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Lesser Leech"
DESC = "At the end of your turn, deal 2 damage to your opponent. Gain lifeforce equal to the damage dealt."
ENERGY = -1


# What happens when you play it
async def turn_func(ply, enemy, data, affected_player):
    if affected_player == "self":
        await mechanics.damage(enemy, 2)
        await mechanics.heal(ply, 2)
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=turn_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
