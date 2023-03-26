from ..aws.ec2 import ec2
from ..aws.ses import ses
from ..config.appConfig import appConfig

def stopMinecraftServer(commandCaller):
    try:
        if(ec2.getInstanceStatus() == "running"):
            ec2.stopInstances()
            ses.sendSimpleEmail(
                appConfig.ALERT_RECIPIENT, 
                buildServerStopAlert(commandCaller)
            )
            return "*The Cum Zone has been put to bed...* 😴🤫"
        else:
            return "The Cum Zone is already sleeping 😴🤫"
    except Exception as e:
        return f'*The Cum Zone won\'t go to sleep* - check with Jacob. Error:\n`{str(e)}`'

def buildServerStopAlert(subject):
    return f'{subject} has stopped the Minecraft Server'