from typing import List
from source.infrastructure.mcstatus.client import mcStatusClient

class QueryServerOfflineResponse:
    type: str

    def __init__(self):
        self.type = "Offline"

class QueryServerOnlineResponse:
    type: str
    now: int
    max: int
    players: List[str]

    def __init__(self, now: int, max: int, players: List[str]):
        self.type = "Online"
        self.now = now
        self.max = max
        self.players = players

async def queryServer() -> QueryServerOfflineResponse | QueryServerOnlineResponse :
    try:
        queryResult = await mcStatusClient.async_query()
        return QueryServerOnlineResponse(
            queryResult.players.online,
            queryResult.players.max,
            queryResult.players.names,
        )
    except:
        return QueryServerOfflineResponse()