from typing import List
from ..infrastructure.mcstatus.queryServer import queryServer, QueryServerOfflineResponse, QueryServerOnlineResponse

class ServerSessionDetails:
    now: int
    max: int
    players: List[str]

    def __init__(self, now: int, max: int, players: List[str]):
        self.now = now
        self.max = max
        self.players = players

    def __str__(self):
        playerString = "".join(self.players)
        return f'{ playerString }'


async def getServerSessionDetails() -> ServerSessionDetails:
    result = await queryServer()
    if type(result) is QueryServerOfflineResponse:
        return ServerSessionDetails(0, 0, [])

    if type(result) is QueryServerOnlineResponse:
        return ServerSessionDetails(
            result.now,
            result.max,
            result.players
        )