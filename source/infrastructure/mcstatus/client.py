from mcstatus import JavaServer

from source.config.appConfig import appConfig

mcStatusClient = JavaServer(
    appConfig.MINECRAFT_SERVER_URL,
    appConfig.MINECRAFT_SERVER_PORT
)