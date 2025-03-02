from source.infrastructure.mcstatus.client import mcStatusClient

class GetStatusOfflineResponse:
    type: str

    def __init__(self):
        self.type = "Offline"

class GetStatusOnlineResponse:
    type: str
    now: int
    max: int

    def __init__(self, now: int, max: int):
        self.type = "Online"
        self.now = now
        self.max = max

async def getStatus() -> GetStatusOfflineResponse | GetStatusOnlineResponse :
    try:
        pingStatus = await mcStatusClient.async_status()
        return GetStatusOnlineResponse(
            pingStatus.players.online,
            pingStatus.players.max
        )
    except Exception as e:
        print(str(e))
        return GetStatusOfflineResponse()