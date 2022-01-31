#!/user/bin/env python

from cardList import addNode
import tcgpowers, mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Electricity"
DESC = "At the start of your turn, deal 2 damage to your opponent."
ENERGY = 2


# What happens when you play it (at the start of your turn)
async def damage_func(ply, enemy, data, affected_player):
    if affected_player == ply:
        await mechanics.damage(enemy, 2)
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=damage_func,
        trigger_type="TURN_START"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
