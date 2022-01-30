import asyncio

from discord.ext.commands import CommandInvokeError


async def is_invoker_registered(ctx):
    """Checks whether a user's data exists."""
    try:
        open('player_data/' + str(ctx.message.author.id) + '.txt', 'r')
        return True
    except Exception as cie:
        await ctx.message.channel.send("You aren't registered! Use =register")
        return False
