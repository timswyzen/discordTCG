#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Maggot Egg"
DESC = "At the start of your turn, sacrifice this Node and spawn a Parasite Node."
ENERGY = 0


# What happens when you play it (at the start of your turn)
async def start_func(ply, enemy, data, affected_player):
    if affected_player == ply:
        await mechanics.sacNode(ply, enemy, ply.nodes.index('Maggot Egg'))
        await ply.addNode('Parasite')
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=start_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
