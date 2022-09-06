from logger import Logger
from server import Init
from core import Registery, Constants
from handler import DiscoveryHandler, MonitoringHandler
from discovery import VcenterDiscovery,HostDiscovery,VmDiscovery
from monitoring import VcenterMonitoring,HostMonitoring,VmMonitoring
from debug import DeviceReachability

from server._controller import app
app = app

def initialize_app():
    Logger().setup_logger_config()
    Registery.RegisterHandlers({Constants.DISCOVERY_HANDLER_IDENTITY:DiscoveryHandler,Constants.MONITORING_HANDLER_IDENTITY:MonitoringHandler})
    Registery.RegisterDiscoveryEntities([VcenterDiscovery,HostDiscovery,VmDiscovery])
    Registery.RegisterMonitoringEntities({'vcenter':VcenterMonitoring,'host':HostMonitoring,'vm':VmMonitoring})
    Registery.RegisterDebugHandlers({Constants.DEVICE_REACHABILITY:DeviceReachability})
    #Init().start_server()

if __name__ == "__main__":
    initialize_app()
else:
    gunicorn_app = initialize_app()