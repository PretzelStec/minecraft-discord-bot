from builtins import bot

from source.domain.stopServer import stopMinecraftServer

@bot.command()
async def stopServer(ctx):
    commandCaller = ctx.author.display_name
    await ctx.send("♬ Go to sleep... Go to sleep, my little Cum Zone ♬")
    statusMessage = stopMinecraftServer(commandCaller)
    await ctx.send(statusMessage)

def setupStopServerCommand():
    bot.add_command(stopServer)