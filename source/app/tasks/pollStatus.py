from builtins import bot

from discord import Status, Game
from discord.ext import tasks

from source.app.tasks.autoShutdown import autoShutdown
from source.config.appConfig import appConfig
from source.domain.getServerStatus import getFormattedStatus, getServerStatus


@tasks.loop(seconds=appConfig.POLL_STATUS_TASK_RATE)
async def pollStatus():
    print("Polling status:")

    botStatus = Status.online
    status = await getServerStatus()
    print(status)

    if(status.status == 0):
        print('Server detected offline')
        botStatus = Status.idle
    if(
        bot.autoShutdownHasStarted == False and 
        status.status == "Online" and
        status.now == 0
    ):
        print('Starting empty server auto shutdown countdown')
        autoShutdown.start()
        bot.autoShutdownHasStarted = True
    elif(bot.autoShutdownHasStarted and status.now != 0):
        print('Cancelling server shutdown')
        autoShutdown.cancel()
        bot.autoShutdownHasStarted = False

    await bot.change_presence(
        status=botStatus,
        activity= Game(getFormattedStatus(status))
    )
    return