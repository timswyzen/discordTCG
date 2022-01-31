#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Foundation"
DESC = "When this is destroyed, sacrifice all your other Nodes."
ENERGY = 1


# What happens when it's sacrificed/killed
async def death_func(ply, enemy):
    for i in range(len(ply.nodes)):
        if not ply.nodes[i] == 'Foundation':
            await mechanics.sacNode(ply, enemy, 0)
    return


FUNC_LIST = [
    NodeFunction(
        func=death_func,
        trigger_type="LTB"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
