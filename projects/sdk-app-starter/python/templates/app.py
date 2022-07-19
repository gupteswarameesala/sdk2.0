from logger import Logger
from server import Init
from core import Registery, Constants
from handler import DiscoveryHandler, MonitoringHandler
from discovery import {{ dm_dic["discovery"] }}
from monitoring import {{ dm_dic["monitoring"] }}
from debug import DeviceReachability

from server._controller import app
app = app

def initialize_app():
    Logger().setup_logger_config()
    Registery.RegisterHandlers({Constants.DISCOVERY_HANDLER_IDENTITY:DiscoveryHandler,Constants.MONITORING_HANDLER_IDENTITY:MonitoringHandler})
    Registery.RegisterDiscoveryEntities([{{dm_dic["discovery"]}}])
    Registery.RegisterMonitoringEntities({{dm_dic["monitoringmap"]}})
    Registery.RegisterDebugHandlers({Constants.DEVICE_REACHABILITY:DeviceReachability})
    #Init().start_server()

if __name__ == "__main__":
    initialize_app()
else:
    gunicorn_app = initialize_app()
