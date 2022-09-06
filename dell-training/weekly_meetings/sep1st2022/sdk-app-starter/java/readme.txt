from logger import Logger
from server import Init
from core import Registery, Constants
from handler import DiscoveryHandler, MonitoringHandler
from discovery import HostDiscovery, VMDiscovery
from monitoring import VMMonitoring,HostMonitoring
def initialize_app():
  Logger().setup_logger_config()
  Registery.RegisterHandlers({Constants.DISCOVERY_HANDLER_IDENTITY:DiscoveryHandler,Constants.MONITORING_HANDLER_IDENTITY:MonitoringHandler})
  Registery.RegiterDiscoveryEntities([HostDiscovery,VMDiscovery])
  Registery.RegisterMonitoringEntities({Constants.VM:VMMonitoring, Constants.HOST:HostMonitoring})
  Init().start_server()
if __name__ == "__main__":
  initialize_app()
