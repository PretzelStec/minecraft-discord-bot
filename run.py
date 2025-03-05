import builtins
import discord
from discord.ext import commands
from source.config.appConfig import appConfig

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)
builtins.bot = bot

# bot.autoShutdownHasStarted = False

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    if appConfig.IS_POLLING_ENABLED:
        pollStatus.start()
    else:
        print("Polling is disabled.")

    if appConfig.IS_BACKUP_ENABLED:
        serverBackup.start()
    else:
        print("Backup is disabled.")


# ----------------
# --- COMMANDS ---
# ----------------

# from source.app.commands.startServer import startServer
# from source.app.commands.stopServer import stopServer
# from source.app.commands.whosOn import whosOn
# setupStartServerCommand()
# setupStopServerCommand()
# setupWhosOnCommand()

# -------------
# --- TASKS ---
# -------------

from source.app.tasks.pollStatus import pollStatus
from source.app.tasks.serverBackup import serverBackup

bot.run(appConfig.DISCORD_TOKEN)