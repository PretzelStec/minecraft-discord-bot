import discord
from discord.ext import commands, tasks
from source.config.appConfig import appConfig
from source.domain.getServerStatus import getServerStatus, getFormattedStatus
from source.domain.startServer import startMinecraftServer
from source.domain.stopServer import stopMinecraftServer

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)
bot.autoShutdownHasStarted = False

@bot.event
async def on_ready():
    pollStatus.start()

# ----------------
# --- COMMANDS ---
# ----------------

@bot.command()
async def startServer(ctx):
    commandCaller = ctx.author.display_name
    await ctx.send("📣WAKE UP CUM ZONE📣")
    statusMessage = startMinecraftServer(commandCaller)
    await ctx.send(statusMessage)

@bot.command()
async def stopServer(ctx):
    commandCaller = ctx.author.display_name
    await ctx.send("♬ Go to sleep... Go to sleep, my little Cum Zone ♬")
    statusMessage = stopMinecraftServer(commandCaller)
    await ctx.send(statusMessage)

# -------------
# --- TASKS ---
# -------------

@tasks.loop(seconds=20)
async def pollStatus():
    print("Polling status:")

    botStatus = discord.Status.online
    status = await getServerStatus()
    print(status)

    if(status.get('max') == 0):
        print('Server detected offline')
        botStatus = discord.Status.idle
    if(
        bot.autoShutdownHasStarted == False and 
        status.get('max') != 0 and 
        status.get('now') == 0
    ):
        print('Starting empty server auto shutdown countdown')
        autoShutdown.start()
        bot.autoShutdownHasStarted = True
    elif(bot.autoShutdownHasStarted and status.get('now') != 0):
        print('Cancelling server shutdown')
        autoShutdown.cancel()
        bot.autoShutdownHasStarted = False

    await bot.change_presence(
        status=botStatus,
        activity=discord.Game(getFormattedStatus(status))
    )
    return

@tasks.loop(minutes=45, count=2)
async def autoShutdown():
    if(autoShutdown.current_loop != 0):
        print("auto shutting down server")
        stopMinecraftServer("Auto Shutdown Task")

bot.run(appConfig.DISCORD_TOKEN)