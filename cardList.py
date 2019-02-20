#!/user/bin/env python

import os
from classes import cardbase, nodebase
import mechanics, random, math

#This file retrieves all cards and nodes for the main game to use

cardsDB = {}
nodesDB = {}

def getCards():
	for filename in os.listdir('cards'):
		exec(open('cards/'+filename).read())
	return cardsDB
	
def getNodes():
	for filename in os.listdir('nodes'):
		exec(open('nodes/'+filename).read())
	return nodesDB

def addCard(name, cost, rarity, desc, targets, cardtype, ability):
	cardsDB[name.lower()] = cardbase.Card(name, cost, rarity, desc, targets, cardtype, ability)
	
def addNode(name, desc, ability, oneTimeAbility, energy, deathFunc):
	nodesDB[name.lower()] = nodebase.GameNode(name, desc, ability, oneTimeAbility, energy, deathFunc)

