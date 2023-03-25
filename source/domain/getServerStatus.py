import requests
from mcstatus import JavaServer

server = JavaServer("minecraft.jacobstec.dev", 25565)

async def getServerStatus():
    global server
    
    status = {"now": 0, "max": 0}

    try:
        pingStatus = await server.async_status()

        status["now"] = pingStatus.players.online
        status["max"] = pingStatus.players.max
    except:
        print("server offline")

    return status

def getFormattedStatus(status):
    if(status.get('max') == 0):
        return 'Offline'
    else: 
        return f'Online { status.get("now") }/{ status.get("max") }'