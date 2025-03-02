from builtins import bot

from discord import Status, Game
from discord.ext import tasks

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

    await bot.change_presence(
        status=botStatus,
        activity= Game(getFormattedStatus(status))
    )
    return