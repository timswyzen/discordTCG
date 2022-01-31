#!/user/bin/env python

from cardList import addNode


# Simple variables
from classes.NodeFunction import NodeFunction

NAME = "Scrambler Trap"
DESC = "When this Node dies, your opponent discards two cards at random."
ENERGY = -1


# What happens when it's sacrificed/killed
async def death_func(ply, enemy, data, affected_player):
    await enemy.randomDiscard()
    await enemy.randomDiscard()
    return


FUNC_LIST = [
    NodeFunction(
        func=death_func,
        trigger_type="LTB"
    )
]

addNode(NAME, DESC, ENERGY, FUNC_LIST)
