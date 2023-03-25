import builtins
import discord
from discord.ext import commands
from source.config.appConfig import appConfig

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="/", intents=intents)
builtins.bot = bot

bot.autoShutdownHasStarted = False

@bot.event
async def on_ready():
    pollStatus.start()

# ----------------
# --- COMMANDS ---
# ----------------

import source.app.commands.startServer
import source.app.commands.stopServer

# -------------
# --- TASKS ---
# -------------

from source.app.tasks.pollStatus import pollStatus

bot.run(appConfig.DISCORD_TOKEN)