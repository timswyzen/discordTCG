#!/user/bin/env python
from random import random

import mechanics
from cardList import addNode


# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Demonic Trap"
DESC = "When this Node is destroyed, destroy an opponent's Node at random."
ENERGY = -1


# What happens when it's sacrificed/killed
async def death_func(ply, enemy, data, affected_player):
    if len(enemy.nodes) > 0:
        target = random.randint(0, len(enemy.nodes) - 1)
        await mechanics.sacNode(enemy, ply, target)


FUNC_LIST = [
    NodeFunction(
        func=death_func,
        trigger_type="LTB"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
