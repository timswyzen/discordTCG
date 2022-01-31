#!/user/bin/env python

from cardList import addNode
import tcgpowers

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Tempter"
DESC = "Passively increases your desperation and hunger by 10."
ENERGY = -6


async def play_func(ply, enemy):
    ply.desperation += 10
    ply.hunger += 10


# What happens when it's sacrificed/killed
async def death_func(ply, enemy):
    ply.desperation -= 10
    ply.hunger -= 10


FUNC_LIST = [
    NodeFunction(
        func=play_func,
        trigger_type="ETB"
    ),
    NodeFunction(
        func=death_func,
        trigger_type="LTB"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
