import asyncio

from discord.ext.commands import CommandInvokeError


@asyncio.coroutine
def is_invoker_registered(ctx):
    """Checks whether a user's data exists."""
    try:
        open('player_data/' + str(ctx.message.author.id) + '.txt', 'r')
        return True
    except Exception as cie:
        yield from ctx.message.channel.send("You aren't registered! Use =register")
        return False
