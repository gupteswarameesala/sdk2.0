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
    def getMonitoringEntity(nativeType):
        return Registery.monitoring_entities[nativeType]

    @staticmethod
    def RegisterHandlers(handlers):
        Registery.handlers = handlers
    
    @staticmethod
    def getHandler(handlerName):
        return Registery.handlers[handlerName]
    
    @staticmethod
    def RegisterDebugHandlers(debugHandlers):
        Registery.debugHandlers = debugHandlers
    
    @staticmethod
    def getDebugHandler(handlerName):
        return Registery.debugHandlers[handlerName]
    
