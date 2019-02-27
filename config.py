#!/user/bin/env python

VERSION = "0.0.4a"

DECK_SIZE_MINIMUM = 40
STARTING_HAND_SIZE = 6
PACK_PRICE = 100
CHALLENGE_TIMEOUT = 30 #How long to wait for someone to accept a challenge
TURN_TIMEOUT = 300 #How long to wait for someone to do an action on their turn before they forfeit the match
TOKEN = '' #secret

DEFINITIONS = {
	"lifeforce": "Your primary resource. You use this to pay card and Node costs. If it reaches 0, you lose.",
	"node": "An object that stays on the board. They can have spawn abilities, death abilities, and abilities that activate on each of your turns.",
	"mill": "Removes the top card of your deck from the game, and you gain lifeforce equal to its cost.",
	"burn": "Removes the top card of your deck from the game. You do not gain lifeforce.",
	"energy": "You gain lifeforce equal to your Energy at the start of each of your turns.",
	"hunger": "Affects how much lifeforce you gain from sacrificing Nodes. You start with 10, and can go down to 0.",
	"desperation": "Affects how much lifeforce you gain from milling. You start with 10, and can go down to 0.",
}

#don't touch
matches = {}
