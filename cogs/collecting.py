#!/user/bin/env python
import discord
from discord.ext import commands
import asyncio, json, os, random
from mechanics import cardList, getPlyData, grantCard, grantMoney, grantPacks, getBal, getPacks
import config
from utils.user import is_invoker_registered


class Collecting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Opening a pack
    @commands.command(pass_context=True)
    async def openpack(self, ctx, *args):
        """OPEN A SHINY NEW PACK!"""

        if not (await is_invoker_registered(ctx)):
            return

        if getPacks(ctx.message.author.id) < 1:
            await ctx.message.channel.send("You don't have any packs to open :( Use =buy to get more!")
            return

        # Grab all the cards
        commons, uncommons, rares = [], [], []
        cardsReceived = []
        for card in cardList:
            if cardList[card].rarity == 'C':
                commons.append(cardList[card].name)
            elif cardList[card].rarity == 'U':
                uncommons.append(cardList[card].name)
            elif cardList[card].rarity == 'R':
                rares.append(cardList[card].name)

        stringToSay = (
            ":star: :star2: :star2: :star2: :star2: :star2: :star2: :star2: :star2: :star2: :star:\n:star: :confetti_ball:           You got new cards!           :confetti_ball: :star:\n")

        # Pick the cards, build the string
        for i in range(5):
            # TODO: can't get 5+ of the same card
            cardsReceived.append(random.choice(commons))
            stringToSay += ":star: Common: " + cardsReceived[i] + "\n"
        for i in range(2):
            cardsReceived.append(random.choice(uncommons))
            stringToSay += ":star: Uncommon: " + cardsReceived[i + 5] + "\n"
        cardsReceived.append(random.choice(rares))
        stringToSay += ":star: :star: **RARE: " + cardsReceived[7] + "**\n"
        stringToSay += ":star: :star2: :star2: :star2: :star2: :star2: :star2: :star2: :star2: :star2: :star:"

        await ctx.message.channel.send(stringToSay)

        # Set their data
        for card in cardsReceived:
            grantCard(ctx.message.author.id, card, 1)
        grantPacks(ctx.message.author.id, -1)

    # Buy packs
    @commands.command(pass_context=True)
    async def buy(self, ctx, amt: int = 1):
        """Buy some packs! =buy <amount>"""
        # Just make sure they can
        if amt < 1:
            await ctx.message.channel.send("Invalid input.")
            return
        if getBal(ctx.message.author.id) < amt * config.PACK_PRICE:
            await ctx.message.channel.send(
                "Not enough money for " + str(amt) + " packs. They are currently $" + str(config.PACK_PRICE) + " each.")
            return
        # Data stuff, then printing
        grantPacks(ctx.message.author.id, amt)
        grantMoney(ctx.message.author.id, -1 * amt * config.PACK_PRICE)
        if amt == 1:
            await ctx.message.channel.send("Bought a pack! Open it with =openpack.")
        else:
            await ctx.message.channel.send("Bought " + str(amt) + " packs!!!! Open them with =openpack!!!!!!!")

    # Checking your packs and $
    @commands.command(pass_context=True)
    async def bal(self, ctx, *args):
        """Get your current balance and amount of packs."""

        if not (await is_invoker_registered(ctx)):
            return

        await ctx.message.channel.send("You currently have $" + str(getBal(ctx.message.author.id)) + " and " + str(
            getPacks(ctx.message.author.id)) + " pack(s).")

    # Trading
    @commands.command(pass_context=True)
    async def trade(self, ctx, target: discord.Member = None, *args):
        """Trade with another user. =trade <@ user>"""

        if not (await is_invoker_registered(ctx)):
            return

        if target == None:
            await ctx.message.channel.send("You must pick someone to trade with! Syntax: =trade <@ user>")
            return
        if ctx.message.author == target:
            await ctx.message.channel.send("Why would you trade with yourself? :confounded:")
            return
        trader, tradee = [], []
        await ctx.message.channel.send("Type 'quit' at any time to quit the trade menu.")
        await ctx.message.channel.send(
            "What are you offering? Syntax: <amount>x <card> or $<money amount>. For example:\n2x Voracity\n$20")

        try:
            message = await self.bot.wait_for('message', check=lambda message: message.author == ctx.message.author,
                                               timeout=90)
        except asyncio.exceptions.TimeoutError:
            ctx.message.channel.send("Timed out waiting for response. Cancelling trade.")
            return

        if message.content.lower().startswith('quit'):
            await ctx.message.channel.send("Quit the trade menu.")
            return

        # Setting up data for trader's offerings
        messageList = message.content.split('\n')
        for idx, line in enumerate(messageList):
            messageList[idx] = line.split('x ')

        playerData = getPlyData(ctx.message.author)

        # Go through the cards and validate, then add to trade
        for cardEntry in messageList:  # for each [2, "caltrops"], for example
            cardPair = None
            # formatting and data getting
            if cardEntry[0][0] == '$':
                with open('player_data/' + str(ctx.message.author.id) + '.txt', 'r') as json_file:
                    traderMoney = json.loads(json_file.read())['money']
                if traderMoney < int(cardEntry[0][1:]) or int(cardEntry[0][1:]) < 0:
                    await ctx.message.channel.send("You don't have enough money.")
                    return
                trader.append(cardEntry[0][1:])
            else:
                try:
                    for item in playerData['collection'].items():
                        if cardEntry[1].lower() == item[0].lower():
                            cardPair = item
                except:
                    await ctx.message.channel.send("Invalid format!")
                    return

                if cardPair == None:
                    await ctx.message.channel.send(cardEntry[1] + " isn't in your collection.")
                    return
                if cardPair[1] < int(cardEntry[0]):
                    await ctx.message.channel.send(
                        "You don't have that many " + cardEntry[1] + " in your collection.")
                    return

                trader.append(cardEntry)

        await ctx.message.channel.send("What do you want in return? (same syntax)")

        try:
            message = await self.bot.wait_for('message', check=lambda message: message.author == ctx.message.author,
                                               timeout=90)
        except asyncio.exceptions.TimeoutError:
            ctx.message.channel.send("Timed out waiting for response. Cancelling trade.")
            return

        if message.content.lower().startswith('quit'):
            await ctx.message.channel.send("Quit the trade menu.")
            return

        # Setting up data for trader's offerings
        messageList = message.content.split('\n')
        for idx, line in enumerate(messageList):
            messageList[idx] = line.split('x ')

        # has data check + data retrieval
        try:
            playerData = getPlyData(target)
        except:
            await ctx.message.channel.send("Target isn't registered yet.")
            return

        # Go through cards and validate, then add to trade
        for cardEntry in messageList:  # for each [2, "caltrops"], for example
            cardPair = None
            # formatting and data getting
            if cardEntry[0][0] == '$':
                with open('player_data/' + str(target.id) + '.txt', 'r') as json_file:
                    tradeeMoney = json.loads(json_file.read())['money']
                if tradeeMoney < int(cardEntry[0][1:]) or int(cardEntry[0][1:]) < 0:
                    await ctx.message.channel.send("He or she doesn't have enough money.")
                    return
                tradee.append(cardEntry[0][1:])
            else:
                try:
                    for item in playerData['collection'].items():
                        if cardEntry[1].lower() == item[0].lower():
                            cardPair = item
                except:
                    await ctx.message.channel.send("Invalid format!")
                    return

                if cardPair == None:
                    await ctx.message.channel.send(cardEntry[1] + " isn't in your collection.")
                    return
                if cardPair[1] < int(cardEntry[0]):
                    await ctx.message.channel.send(
                        "You don't have that many " + cardEntry[1] + " in your collection.")
                    return

                tradee.append(cardEntry)
        # wow that was a lot. let's get the other user's approval then do the trade now.
        print(str(trader) + " | " + str(tradee))

        def check(author):
            def inner_check(msg):
                return (msg.content.lower().startswith('yes') or msg.content.lower().startswith(
                    'no')) and msg.author == author

        await ctx.message.channel.send(target.name + ": Do you accept the above trade? ('yes' or 'no')")
        try:
            message = await self.bot.wait_for('message', check=check(ctx.message.author), timeout=30)
        except asyncio.exceptions.TimeoutError:
            ctx.message.channel.send("Timed out waiting for response. Cancelling trade.")
            return

        if message.content.lower().startswith('no'):
            await ctx.message.channel.send("Trade request denied.")
            return
        # Complete the trade
        elif message.content.lower().startswith('yes'):
            # give trader the tradee's stuff
            for item in tradee:
                if isinstance(item, str):
                    grantMoney(ctx.message.author.id, int(item))
                    grantMoney(target.id, -1 * int(item))
                else:
                    grantCard(target.id, item[1], -1 * int(item[0]))
                    grantCard(ctx.message.author.id, item[1], item[0])
            # give tradee the trader's stuff
            for item in trader:
                if isinstance(item, str):
                    grantMoney(ctx.message.author.id, -1 * int(item))
                    grantMoney(target.id, int(item))
                else:
                    grantCard(target.id, item[1], item[0])
                    grantCard(ctx.message.author.id, item[1], -1 * int(item[0]))
            await ctx.message.channel.send("Trade complete!")


def setup(bot):
    bot.add_cog(Collecting(bot))
