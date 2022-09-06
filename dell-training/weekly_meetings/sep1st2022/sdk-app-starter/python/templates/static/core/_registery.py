

class Registery:

    handlers = {}
    discovery_entities = []
    monitoring_entities = {}

    debugHandlers = {}

    @staticmethod
    def RegisterDiscoveryEntities(discovery_entities):
        Registery.discovery_entities = discovery_entities

    @staticmethod
    def RegisterMonitoringEntities(monitoring_entities):
        Registery.monitoring_entities = monitoring_entities

    @staticmethod
    def getDiscoveryEntities():
        return Registery.discovery_entities

    @staticmethod
    def getMonitoringEntity(nativetype):
        return Registery.monitoring_entities[nativetype]

    @staticmethod
    def RegisterHandlers(handlers):
        Registery.handlers = handlers

    @staticmethod
    def getHandler(handlername):
        return Registery.handlers[handlername]

    @staticmethod
    def RegisterDebugHandlers(debughandlers):
        Registery.debugHandlers = debughandlers

    @staticmethod
    def getDebugHandler(handlername):
        return Registery.debugHandlers[handlername]
