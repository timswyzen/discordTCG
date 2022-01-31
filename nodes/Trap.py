#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Trap"
DESC = "When destroyed, deal 3 damage to your opponent."
ENERGY = 0


# What happens when it's sacrificed/killed
async def death_func(ply, enemy, data, affected_player):
    await mechanics.damage(enemy, 3)


FUNC_LIST = [
    NodeFunction(
        func=death_func,
        trigger_type="LTB"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
