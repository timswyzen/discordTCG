#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Defiance"
DESC = "Whenever your opponent spawns a Node, deal 3 damage to them."
ENERGY = -1


# What happens when the TRIGGER is triggered
async def trigger_func(ply, enemy, data, affectedPlayer):
    if affectedPlayer == "enemy":
        await mechanics.damage(enemy, 3)
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=trigger_func,
        trigger_type="NODESPAWN"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
