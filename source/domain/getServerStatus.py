from source.infrastructure.mcstatus.getStatus import getStatus, GetStatusOfflineResponse, GetStatusOnlineResponse

class GetServerStatusResponse:
    status: str
    now: int
    max: int

    def __init__(self, status: str, now: int = 0, max: int = 0):
        self.status = status
        self.now = now
        self.max = max

    def __str__(self):
        return f'{self.status} - {self.now}/{self.max}'

async def getServerStatus() -> GetServerStatusResponse:    
    result = await getStatus()

    if(type(result) is GetStatusOfflineResponse):
        return GetServerStatusResponse("Offline")
    if(type(result) is GetStatusOnlineResponse): 
        return GetServerStatusResponse("Online", result.now, result.max)

def getFormattedStatus(result: GetServerStatusResponse) -> str:
    if(result.status == "Offline"):
        return 'Offline'
    if(result.status == "Online"): 
        return f'Online { result.now }/{ result.max }'
