from builtins import bot

from source.domain.getServerSessionDetails import getServerSessionDetails, ServerSessionDetails

@bot.command()
async def whosOn(ctx):
    result = await getServerSessionDetails()

    string = "No one is online"
    if(result.now > 0):
        string = str(result)

    await ctx.send(string)

def setupWhosOnCommand():
    bot.add_command(whosOn)