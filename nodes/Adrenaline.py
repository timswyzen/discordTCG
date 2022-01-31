#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Adrenaline"
DESC = "At the start of your turn, if you have less than 15 lifeforce, sacrifice this Node and gain 5 lifeforce and 5 Desperation."
ENERGY = -1


# What happens when you play it (at the start of your turn)
async def sac_func(ply, enemy, data, affected_player):
    if affected_player == "self":
        if ply.lifeforce < 15:
            await mechanics.heal(ply, 5)
            ply.desperation += 5
            await mechanics.sacNode(ply, enemy, ply.nodes.index('Adrenaline'))
        return
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=sac_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
