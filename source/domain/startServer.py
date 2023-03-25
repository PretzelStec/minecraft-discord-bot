from ..aws.ec2 import ec2
from ..aws.ses import ses
from ..config.appConfig import appConfig

def startMinecraftServer(commandCaller):
    try:
        if(ec2.getInstanceStatus() == "stopped"):
            ec2.startInstances()
            ses.sendSimpleEmail(
                appConfig.ALERT_RECIPIENT,
                buildServerStartAlert(commandCaller)
            )
            return "*The Cum Zone has been awoken...*"
        else:
            return "The Cum Zone is already awake, pay attention, please 🤨"
    except Exception as e:
        return f'*The Cum Zone won\'t wake up* - check with Jacob. Error:\n`{str(e)}`'

def buildServerStartAlert(subject):
    return f'{subject} has started the Minecraft Server'