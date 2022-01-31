#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Supplies"
DESC = "When destroyed, gain 5 lifeforce."
ENERGY = 0


# What happens when it's sacrificed/killed
async def death_func(ply, enemy, data, affected_player):
    await mechanics.heal(ply, 5)
    return


FUNC_LIST = [
    NodeFunction(
        func=death_func,
        trigger_type="LTB"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
