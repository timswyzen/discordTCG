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
	
#Currently unused function to give all players $100
def theHandout():
	for files in os.listdir('player_data'):
		with open('player_data/'+str(files)+'.txt', 'r') as json_file: 
			fileContents = json.loads(json_file.read())
		fileContents['money'] += 100
		with open('player_data/'+str(files)+'.txt', 'w') as outfile:
			json.dump(fileContents, outfile)
	print( "Gave each player $100." )

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
		ply.lifeforce += healthToGain
	ply.energy -= removedNode.energy
	gameTrigger( "SAC", ply, removedNode )
	return removedNode
	
#Player milled a card for health
def millCard( ply ):
	poppedCard = ply.deck.pop()
	cost = cardList[poppedCard.lower()].cost
	lifeToGain = abs(round( 0.1 * ply.desperation * cost ))
	ply.lifeforce += lifeToGain
	gameTrigger( "MILL", ply, None )
	return poppedCard, lifeToGain
	
#Player activated a node
def activateNode( nodeName, activePlayerObj, opponentObj, activePlayer, otherPlayer, matches, bot ):
	playedObject = nodeList[nodeName.lower()]
	playedObject.func( activePlayerObj, opponentObj )
	
#Game ended
def gameOver( winner, loser, matches, bot, ctx ):
	print(str(matches))
	if winner.name in matches:
		matchWager = matches[winner.name].wager
		matchTime = matches[winner.name].startTime
		del matches[winner.name]
	elif loser.name in matches:
		matchWager = matches[loser.name].wager
		matchTime = matches[loser.name].startTime
		del matches[loser.name]
	yield from mechMessage( bot, ctx.message.channel, ":medal: " + loser.name + " just lost to " + winner.name + " in discordTCG!" )
	grantMoney(winner.id, matchWager)
	grantMoney(loser.id, -1*matchWager)
	#random money pickup chance
	secondsElapsed = time.time()-matchTime
	if secondsElapsed > 127:
		if random.randint(0,4)%2 == 1:
			givenMoney = random.randint( 15, 40 )
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
		
#Give someone an amount of a card (takes their discord ID)
def grantCard( plyID, card, amount ): 
	with open('player_data/'+str(plyID)+'.txt', 'r') as json_file: 
		fileContents = json.loads(json_file.read())
		
	foundCard = False
	for cards in fileContents['collection']:
		if card.lower() == cards.lower():
			foundCard = True
			fileContents['collection'][cards] += int(amount)
	if foundCard == False:
		fileContents['collection'][cardList[card.lower()].name] = 1
			
	with open('player_data/'+str(plyID)+'.txt', 'w') as outfile:
		json.dump(fileContents, outfile)
	
#Get someone's $  (takes discord ID)	
def getBal( plyID ):
	with open('player_data/'+str(plyID)+'.txt', 'r') as json_file:
		return json.loads(json_file.read())['money']

#Give some money (Takes discord ID)
def grantMoney( plyID, amount ):
	with open('player_data/'+str(plyID)+'.txt', 'r') as json_file: 
		fileContents = json.loads(json_file.read())
		
	fileContents['money'] += amount
			
	with open('player_data/'+str(plyID)+'.txt', 'w') as outfile:
		json.dump(fileContents, outfile)
	
#Get someone's amount of packs (takes discord ID)	
def getPacks( plyID ):
	with open('player_data/'+str(plyID)+'.txt', 'r') as json_file:
		return json.loads(json_file.read())['packs']
	
#Grants someone some packs (takes discord ID)	
def grantPacks( plyID, amount ):
	with open('player_data/'+str(plyID)+'.txt', 'r') as json_file: 
		fileContents = json.loads(json_file.read())
		
	fileContents['packs'] += amount
			
	with open('player_data/'+str(plyID)+'.txt', 'w') as outfile:
		json.dump(fileContents, outfile)

#Automates damage dealing
def damage( playerObj, amt ):
	playerObj.lifeforce -= amt
	gameTrigger( "DAMAGE", playerObj, amt )
	
#Automates lifegain
def heal( playerObj, amt ):
	playerObj.lifeforce += amt
	gameTrigger( "HEAL", playerObj, amt )
		
"""Handle triggers. 
dataPassed is the node destroyed/created, damage dealt/healed, etc
playerObj is the player who was affected. This means loop through both still for Node checking.
Make sure to print out using the new mechMessage() so people know what was triggered.
Could also use this to log!
Possible triggers: "HEAL", "DAMAGE", "BURN", "MILL", "SAC", "NODESPAWN"
"""
def gameTrigger( trigger, playerObj, dataPassed ):
	for node in playerObj.nodes:
		if nodeList[node.lower()].triggerType == trigger:
			nodeList[node.lower()].triggerFunc( playerObj, playerObj.opponent )
	for node in playerObj.opponent.nodes:
		if nodeList[node.lower()].triggerType == trigger:
			nodeList[node.lower()].triggerFunc( playerObj.opponent, playerObj )
