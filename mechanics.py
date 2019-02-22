#!/user/bin/env python

from cardList import getCards, getNodes
import json, asyncio, math, time, random

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
	
#Give $100 every Sunday at noon (TODO: Make sure this works!)
def theHandout():
	for files in os.listdir('player_data'):
		with open('player_data/'+str(files)+'.txt', 'r') as json_file: 
			fileContents = json.loads(json_file.read())
		fileContents['money'] += 100
		with open('player_data/'+str(files)+'.txt', 'w') as outfile:
			json.dump(fileContents, outfile)

#Handling bot messages outside the bot files
@asyncio.coroutine
def mechMessage( bot, ctx, msg ):
	yield from bot.send_message( ctx, msg )
		
#Handles a Node entering the field 
def nodeETB( ply, nodeName ):
	nodeObj = nodeList[ nodeName.lower() ]
	nodeObj.spawnFunc(ply,ply.opponent)
	ply.energy = ply.energy + nodeObj.energy
	
#Player sacrificed a node as part of an ability (for health)	
def sacNode( ply, enemy, index ): #Returns the node OBJECT, not the name.
	removedNode = nodeList[ply.nodes[index].lower()]
	removedNode.deathFunc( ply, enemy ) #gets rid of temp effects n stuff
	ply.nodes.remove( ply.nodes[index] )
	healthToGain = abs(round( 0.1 * ply.hunger * removedNode.energy ))
	if 'Feast' not in ply.nodes and 'Feast' not in enemy.nodes: #card...specific......
		ply.lifeforce = ply.lifeforce + healthToGain
	ply.energy = ply.energy - removedNode.energy
	return removedNode
	
#Player milled a card for health
def millCard( ply ):
	poppedCard = ply.deck.pop()
	cost = cardList[poppedCard.lower()].cost
	lifeToGain = abs(round( 0.1 * ply.desperation * cost ))
	ply.lifeforce = ply.lifeforce + lifeToGain
	return poppedCard, lifeToGain
	
#Player activated a node
def activateNode( nodeName, activePlayerObj, opponentObj, matches ):
	playedObject = nodeList[nodeName.lower()]
	playedObject.func( activePlayerObj, opponentObj )
	
	if opponentObj.lifeforce <= 0:
		gameOver( activePlayerObj, opponentObj, matches )
	elif activePlayerObj.lifeforce <= 0:
		gameOver( opponentObj, activePlayerObj, matches )
	
#Game ended
def gameOver( winner, loser, matches, bot ):
	if winner.name in matches:
		match = matches[winner.name]
		del matches[winner.name]
	elif loser.name in matches:
		match = matches[loser.name]
		del matches[loser.name]
	grantMoney(winner.id, match.wager)
	grantMoney(loser.id, -1*match.wager)
	#random money pickup chance
	secondsElapsed = time.time()-match.startTime
	if secondsElapsed > 127:
		if random.randint(0,4)%2 == 1:
			givenMoney = random.randint( 1, 12 )
			grantMoney( winner.id, givenMoney )
			yield from mechMessage( bot, winner, "You found $" + str(givenMoney) + " lying in your opponent's ashes." )
		
#Get player object from just a name (may bug out if the game gets too big because of duplicate names)
def searchPlayerInMatch( playerName, match ):
	#Returns the player object for the searched player
	if match.chalObj.name == playerName:
		return match.chalObj
	elif match.defObj.name == playerName:
		return match.defObj
	else:
		return None
		
def grantCard( plyID, card, amount ): 
	with open('player_data/'+str(plyID)+'.txt', 'r') as json_file: 
		fileContents = json.loads(json_file.read())
		
	for cards in fileContents['collection']:
		if card.lower() == cards.lower():
			fileContents['collection'][cards] += int(amount)
			
	with open('player_data/'+str(plyID)+'.txt', 'w') as outfile:
		json.dump(fileContents, outfile)
		
def getBal( plyID ):
	with open('player_data/'+str(plyID)+'.txt', 'r') as json_file:
		return json.loads(json_file.read())['money']

def grantMoney( plyID, amount ):
	with open('player_data/'+str(plyID)+'.txt', 'r') as json_file: 
		fileContents = json.loads(json_file.read())
		
	fileContents['money'] += amount
			
	with open('player_data/'+str(plyID)+'.txt', 'w') as outfile:
		json.dump(fileContents, outfile)
		
def getPacks( plyID ):
	with open('player_data/'+str(plyID)+'.txt', 'r') as json_file:
		return json.loads(json_file.read())['packs']
		
def grantPacks( plyID, amount ):
	with open('player_data/'+str(plyID)+'.txt', 'r') as json_file: 
		fileContents = json.loads(json_file.read())
		
	fileContents['packs'] += amount
			
	with open('player_data/'+str(plyID)+'.txt', 'w') as outfile:
		json.dump(fileContents, outfile)
