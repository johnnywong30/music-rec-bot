from bot.client import bot


@bot.command()
async def ping(ctx):
    await ctx.send("pong")
