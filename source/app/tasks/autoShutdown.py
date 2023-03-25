from discord.ext import tasks

from source.domain.stopServer import stopMinecraftServer

@tasks.loop(minutes=45, count=2)
async def autoShutdown():
    if(autoShutdown.current_loop != 0):
        print("auto shutting down server")
        stopMinecraftServer("Auto Shutdown Task")