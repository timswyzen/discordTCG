#!/user/bin/env python

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
import os, sys, random
from classes import cardbase, gamebase, playerbase
import mechanics, config
import json

# For cogs when needed
mechanics.initData()
startup_extensions = ['cogs.infocommands', 'cogs.deckbuilding', 'cogs.collecting']
config.matches = {}

# Bot setup
TOKEN = config.TOKEN
bot = commands.Bot(command_prefix='=')


# Load extensions
@bot.event
@asyncio.coroutine
def on_ready():
    yield from bot.change_presence(
        status='Version ' + config.VERSION)  # TODO: show current # matches once this gets bigger xd
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print("Successfully loaded " + str(extension) + "!")
        except Exception as e:
            print("Extension load failed: " + str(extension) + ".\nMessage: " + str(e))


# Send hand function
@asyncio.coroutine
def sendHand(player, playerObj, ctx):
    # delete last hand sent
    if not playerObj.lastHandDM == None:
        yield from playerObj.lastHandDM.delete()

    # send hand
    stringSend = ""
    for cards in playerObj.hand:
        stringSend += str(mechanics.cardList[cards.lower()]) + "\n"
    playerObj.lastHandDM = yield from player.send("[-----Hand-----]\n" + stringSend + "\n\n")


# print and reset player logs, then activate all triggered abilities
@asyncio.coroutine
def printLogs(match, ctx):
    playerOneObj = match.chalObj
    playerTwoObj = match.defObj

    strToSend = ""
    for logs in playerOneObj.log:
        strToSend += logs + '\n'
    if len(playerOneObj.log) > 0:
        yield from ctx.message.channel.send(strToSend)
    playerOneObj.log = []

    strToSend = ""
    for logs in playerTwoObj.log:
        strToSend += logs + '\n'
    if len(playerTwoObj.log) > 0:
        yield from ctx.message.channel.send(strToSend)
    playerTwoObj.log = []


# Active player played a card
@asyncio.coroutine
def playCard(match, activePlayer, activePlayerObj, opponent, opponentObj, cardName, targets, ctx):
    playedObject = mechanics.cardList[cardName.lower()]

    # Pay health if possible
    if activePlayerObj.lifeforce <= playedObject.cost:
        yield from ctx.message.channel.send("You don't have enough lifeforce for that card.")
        return
    else:
        activePlayerObj.lifeforce -= playedObject.cost  # doesn't use damage function cause it shouldn't trigger as damage

    if activePlayerObj.lifeforce <= 0:
        yield from gameOver(activePlayer.id)
        return

    # Remove card from hand
    for card in activePlayerObj.hand:
        if card.lower() == cardName:
            activePlayerObj.hand.remove(card)
            break

    # Play the card (assuming already got proper targets)
    yield from playedObject.func(activePlayerObj, opponentObj,
                                 targets) or []  # the or [] does something undefined but makes it work.
    # TODO: figure out why 'or []' works LMAO
    yield from ctx.message.channel.send(activePlayer.name + " played " + str(playedObject) + "\n\n")
    mechanics.add_to_trigger_queue("PLAYED_CARD", activePlayerObj, playedObject.name)

    # check if game still exists
    if not mechanics.isGameRunning(match):
        return

    # Send hand & messages
    activePlayerObj.cardsThisTurn += 1
    yield from sendHand(activePlayer, activePlayerObj, ctx)

    yield from printLogs(match, ctx)
    if not match.gameMessage == None:
        yield from match.gameMessage.delete()
    match.gameMessage = yield from ctx.message.channel.send(
        str(activePlayerObj) + "\n\n" + str(opponentObj) + "\nCommands: play, concede, pass, info, mill")
    return True


@asyncio.coroutine
def getTarget(playedObject, activePlayerObj, activePlayer, otherPlayerObj, ctx):
    targetEmojis = ['0⃣', '1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
    if playedObject.targets == None:
        return None
    elif playedObject.targets == "ENEMY_NODE":
        # React to self up to amount of enemy nodes (if none, then continue big loop)
        if len(otherPlayerObj.nodes) == 0:
            yield from ctx.message.channel.send("No nodes to target.")
            return -1  # if False, continue

        msg = yield from ctx.message.channel.send("Use reactions to indicate which of your opponent's Nodes to target.")
        for i in range(len(otherPlayerObj.nodes)):
            yield from bot.add_reaction(msg, targetEmojis[i + 1])

        # Wait for reaction from that list
        res = yield from bot.wait_for_reaction(emoji=targetEmojis, message=msg, user=activePlayer)
        thisTarget = targetEmojis.index(str(res.reaction.emoji)) - 1
        return thisTarget
    elif playedObject.targets == "FRIENDLY_NODE":
        # React to self up to amount of friendly nodes (if none, then continue big loop)
        if len(activePlayerObj.nodes) == 0:
            yield from ctx.message.channel.send("No nodes to target.")
            return -1

        msg = yield from ctx.message.channel.send("Use reactions to indicate which of your Nodes to target.")
        for i in range(len(activePlayerObj.nodes)):
            yield from bot.add_reaction(msg, targetEmojis[i + 1])

        # Wait for reaction from that list
        res = yield from bot.wait_for_reaction(emoji=targetEmojis, message=msg, user=activePlayer)
        thisTarget = targetEmojis.index(str(res.reaction.emoji)) - 1
        return thisTarget

    elif playedObject.targets == "PLAYER":
        msg = yield from ctx.message.channel.send(
            "Use reactions to indicate which player to target (1 is yourself, 2 is your opponent).")
        for i in range(2):
            yield from bot.add_reaction(msg, targetEmojis[i + 1])
        res = yield from bot.wait_for_reaction(emoji=targetEmojis, message=msg, user=activePlayer)
        thisTarget = targetEmojis.index(str(res.reaction.emoji)) - 1
        return thisTarget


# New round in a match started
@asyncio.coroutine
def startRound(match, activePlayer, activePlayerObj, otherPlayer, otherPlayerObj, ctx):
    # check if game still exists
    if not mechanics.isGameRunning(match):
        return
    # check if milled out when drawing a card (maybe condense this chunk somehow)
    if not activePlayerObj.drawCard():
        yield from ctx.message.channel.send(activePlayer.name + " milled out!")
        yield from mechanics.gameOver(activePlayer.id)
        return

    # Energy costs (oooh actual phase orders are showing c:)
    yield from mechanics.heal(activePlayerObj, activePlayerObj.energy)

    # check if game still exists
    if not mechanics.isGameRunning(match):
        return

    # Activate all of active player's nodes/initialize turn-based vars
    if len(activePlayerObj.nodes) > 0:
        for thisNode in activePlayerObj.nodes.copy():
            yield from mechanics.activateNode(thisNode, activePlayerObj, otherPlayerObj)
        yield from ctx.message.channel.send(activePlayerObj.name + " activated their start of turn abilities.")
    activePlayerObj.newTurn()
    otherPlayerObj.newTurn()
    activePlayerObj.newMyTurn()

    # check if game still exists
    if not mechanics.isGameRunning(match):
        return

    # Send the info
    yield from ctx.message.channel.send(activePlayer.name + "'s turn.")
    if not match.gameMessage == None:
        yield from match.gameMessage.delete()
    yield from printLogs(match, ctx)
    match.gameMessage = yield from ctx.message.channel.send(
        str(activePlayerObj) + "\n\n" + str(otherPlayerObj) + "\nCommands: play, concede, pass, info, mill")

    yield from sendHand(activePlayer, activePlayerObj, ctx)

    # Make sure it's a game command
    def check_command(msg):
        return msg.author == activePlayer and (msg.content.lower().startswith('play') or msg.content.lower().startswith(
            'concede') or msg.content.lower().startswith('pass') or msg.content.lower().startswith(
            'info') or msg.content.lower().startswith('mill'))

    # Wait for active player's command.
    while True:
        # check if game still exists
        if not mechanics.isGameRunning(match):
            return

        messageOriginal = yield from bot.wait_for('message', check=check_command, timeout=config.TURN_TIMEOUT)

        # Act within 500 seconds or game is lost
        try:
            message = messageOriginal.content.lower().split(' ', 1)
        except AttributeError:
            yield from ctx.message.channel.send("Game timed out!")
            match.timedOut = True
            yield from mechanics.gameOver(activePlayer.id)
            break

        if message[0] == 'info':
            if not match.gameMessage == None:
                yield from match.gameMessage.delete()
            match.gameMessage = yield from ctx.message.channel.send(
                str(activePlayerObj) + "\n\n" + str(otherPlayerObj) + "\nCommands: play, concede, pass, info, mill")
            continue
        elif message[0] == 'play':  # The big one

            # Ensure it's in hand
            if not any(message[1] in x.lower() for x in activePlayerObj.hand):
                yield from ctx.message.channel.send("Played an invalid card.")
                continue

            # Get proper targets
            playedObject = mechanics.cardList[message[1].lower()]
            thisTarget = yield from getTarget(playedObject, activePlayerObj, activePlayer, otherPlayerObj, ctx)
            if thisTarget == -1:
                continue

            # Check if node generator (for 1 per turn limit)
            if playedObject.cardtype == "NodeGen":
                if activePlayerObj.playedNode:
                    yield from ctx.message.channel.send("You already spawned a Node this turn.")
                    continue
                else:
                    activePlayerObj.playedNode = True
            yield from playCard(match, activePlayer, activePlayerObj, otherPlayer, otherPlayerObj, message[1],
                                thisTarget, ctx)
            continue

        elif message[0] == 'pass':
            yield from startRound(match, otherPlayer, otherPlayerObj, activePlayer, activePlayerObj, ctx)
            break
        elif message[0] == 'mill':
            if activePlayerObj.milled == True:
                yield from ctx.message.channel.send("You already milled a card this turn.")
                continue
            elif len(activePlayerObj.deck) <= 0:
                yield from ctx.message.channel.send("You have no cards to mill.")
                continue
            else:
                activePlayerObj.milled = True
                poppedCard, lifeToGain = mechanics.millCard(activePlayerObj)
                yield from ctx.message.channel.send(
                    activePlayerObj.name + " milled " + poppedCard + " for " + str(lifeToGain) + " health.")
                continue
        elif message[0] == 'concede':
            yield from ctx.message.channel.send(activePlayer.name + " conceded.")
            yield from mechanics.gameOver(activePlayer.id)
            return


# Challenge someone and initialize the fight
@bot.command(pass_context=True)
@asyncio.coroutine
def challenge(ctx, target: discord.Member = None, *args):
    """Challenge a friend to discordTCG! =challenge <@user> <wager>"""

    challengerID = ctx.message.author.id

    # Make sure neither player is in a game currently
    if challengerID in config.matches or target.id in config.matches:
        yield from ctx.message.channel.send("A player is already in a match.")
        return

    # Dont challenge yourself man
    if ctx.message.author == target:
        yield from ctx.message.channel.send("You can't challenge yourself, silly!")
        return

    # Have challenged guy accept
    yield from ctx.message.channel.send(target.name + ", you've been challenged to a discordTCG match! Type 'accept' to accept.")

    def check(m):
        return m.author == target and m.content == 'accept'

    message = yield from bot.wait_for('message', check=check, timeout=config.CHALLENGE_TIMEOUT)
    if message is None:
        yield from ctx.message.channel.send(ctx.message.author.name + ", your challenge was not accepted :(")
        return

    # check again here for duplicate accepts
    if challengerID in config.matches or target.id in config.matches:
        yield from ctx.message.channel.send("A player is already in a match.")
        return

    # Get player data
    challengerDeck = mechanics.getPlyData(ctx.message.author)
    defenderDeck = mechanics.getPlyData(target)
    if defenderDeck is None or challengerDeck is None:
        yield from ctx.message.channel.send("Both players aren't registered! Use =register.")
        return
    challengerDeck = challengerDeck['decks'][challengerDeck['selectedDeck']]
    defenderDeck = defenderDeck['decks'][defenderDeck['selectedDeck']]
    if len(challengerDeck) < config.DECK_SIZE_MINIMUM or len(defenderDeck) < config.DECK_SIZE_MINIMUM:
        yield from ctx.message.channel.send(
            "A player doesn't have at least " + str(config.DECK_SIZE_MINIMUM) + " cards in his or her deck.")
        return

    # Wager stuff
    try:
        wager = int(args[0])
        if mechanics.getBal(ctx.message.author.id) < wager or mechanics.getBal(target.id) < wager:
            yield from ctx.message.channel.send("A player doesn't have enough money for this wager!")
            return
        yield from ctx.message.channel.send("Wager set to $" + args[0] + "!")
    except:
        wager = 0

    # Initialize game
    # TODO: [challenger] -> [ctx.message.author.id]
    config.matches[challengerID] = gamebase.TCGame(challengerID, target.id, wager)
    config.matches[challengerID].chalObj = playerbase.Player(ctx.message.author.name, challengerDeck, [], bot, ctx)
    config.matches[challengerID].defObj = playerbase.Player(target.name, defenderDeck, [], bot, ctx)
    config.matches[challengerID].chalObj.shuffle()
    config.matches[challengerID].defObj.shuffle()
    for i in range(config.STARTING_HAND_SIZE):
        config.matches[challengerID].chalObj.drawCard()
        config.matches[challengerID].defObj.drawCard()
    config.matches[challengerID].chalObj.opponent = config.matches[challengerID].defObj
    config.matches[challengerID].defObj.opponent = config.matches[challengerID].chalObj
    print('A match has started. ' + str(ctx.message.author.name) + ' vs ' + str(target.name) + '!')

    # Start round
    if random.randint(0, 1) == 0:
        config.matches[challengerID].chalObj.active = True
        config.matches[challengerID].defObj.energy += 1
        yield from startRound(config.matches[challengerID], ctx.message.author, config.matches[challengerID].chalObj,
                              target, config.matches[challengerID].defObj, ctx)
    else:
        config.matches[challengerID].defObj.active = True
        config.matches[challengerID].chalObj.energy += 1
        yield from startRound(config.matches[challengerID], target, config.matches[challengerID].defObj,
                              ctx.message.author, config.matches[challengerID].chalObj, ctx)


print("[-=-Loaded Cards-=-]\n")
for cards in mechanics.cardList:
    print(cards)
print("\n[-=-Loaded Nodes-=-]\n")
for nodes in mechanics.nodeList:
    print(nodes)

bot.run(TOKEN)
