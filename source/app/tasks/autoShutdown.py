# from discord.ext import tasks
# from source.config.appConfig import appConfig
# from source.domain.stopServer import stopMinecraftServer

# @tasks.loop(minutes=appConfig.AUTO_SHUTDOWN_TASK_TIMER, count=2)
# async def autoShutdown():
#     if(autoShutdown.current_loop != 0):
#         print("auto shutting down server")
#         stopMinecraftServer("Auto Shutdown Task")
