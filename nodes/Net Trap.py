#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics, random

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Net Trap"
DESC = "When this is destroyed, steal a random enemy Node."
ENERGY = -2


# What happens when it's sacrificed/killed
async def death_func(ply, enemy, data, affected_player):
    if len(enemy.nodes) > 0:
        target = random.randint(0, len(enemy.nodes) - 1)
        nodeType = mechanics.nodeList[enemy.nodes[target].lower()]
        await ply.addNode(enemy.nodes[target])
        enemy.energy -= nodeType.energy
        enemy.nodes.pop(target)


FUNC_LIST = [
    NodeFunction(
        func=death_func,
        trigger_type="LTB"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
