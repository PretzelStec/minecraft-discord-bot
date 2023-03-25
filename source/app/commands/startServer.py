from builtins import bot

from source.domain.startServer import startMinecraftServer

@bot.command()
async def startServer(ctx):
    commandCaller = ctx.author.display_name
    await ctx.send("📣WAKE UP CUM ZONE📣")
    statusMessage = startMinecraftServer(commandCaller)
    await ctx.send(statusMessage)