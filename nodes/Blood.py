#!/user/bin/env python

from cardList import addNode
import mechanics

# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Blood"
DESC = "Whenever you damage your opponent, heal that much lifeforce."
ENERGY = -3


# What happens when the TRIGGER is triggered
async def damage_func(ply, enemy, dataPassed, affectedPlayer):
    # dataPassed is damage dealt
    if affectedPlayer == "enemy":
        await mechanics.heal(ply, dataPassed)
    else:
        return False


FUNC_LIST = [
    NodeFunction(
        func=damage_func,
        trigger_type="DAMAGE"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
