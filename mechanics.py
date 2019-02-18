#!/user/bin/env python

from cardList import getCards, getNodes
import json, asyncio, math

"""Extra functions that work better in their own file"""

def initData():
	global cardList
	cardList = getCards() 
	global nodeList
	nodeList = getNodes()

#Retrieve account information
def getPlyData( ply ): #takes a discord user object, not game object
	try:
		with open('player_data/'+str(ply.id)+'.txt', 'r') as json_file: 
			return json.loads(json_file.read())
	except:
		return None
	
#Player sacrificed a node as part of an ability (for health)	
def sacNode( ply, enemy, index ): #Returns the node OBJECT, not the name.
	removedNode = nodeList[ply.nodes[index].lower()]
	removedNode.deathFunc( ply, enemy ) #gets rid of temp effects n stuff
	ply.nodes.remove( ply.nodes[index] )
	healthToGain = abs(math.ceil( ply.hunger * removedNode.energy ))
	ply.lifeforce = ply.lifeforce + healthToGain
	ply.energy = ply.energy - removedNode.energy
	return removedNode
	
#Player milled a card for health
def millCard( ply ):
	poppedCard = ply.deck.pop()
	cost = cardList[poppedCard.lower()].cost
	lifeToGain = abs(math.ceil( ply.desperation * cost ))
	ply.lifeforce = ply.lifeforce + lifeToGain
	
#Player activated a node
def activateNode( nodeName, activePlayerObj, opponentObj, matches ):
	playedObject = nodeList[nodeName.lower()]
	playedObject.func( activePlayerObj, opponentObj )
	
	if opponentObj.lifeforce <= 0:
		gameOver( activePlayerObj, opponentObj, matches )
	elif activePlayerObj.lifeforce <= 0:
		gameOver( opponentObj, activePlayerObj, matches )
	
#Game ended
def gameOver( winner, loser, matches ):
	if winner.name in matches:
		del matches[winner.name]
	elif loser.name in matches:
		del matches[loser.name]
		
#Get player object from just a name (may bug out if the game gets too big because of duplicate names)
def searchPlayerInMatch( playerName, match ):
	#Returns the player object for the searched player
	if match.chalObj.name == playerName:
		return match.chalObj
	elif match.defObj.name == playerName:
		return match.defObj
	else:
		return None
