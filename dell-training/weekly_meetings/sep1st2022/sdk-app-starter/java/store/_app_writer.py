import os


def writefile():
    lines = []
    lines.append('from logger import Logger')
    lines.append('from server import Init')
    lines.append('from core import Registery, Constants')
    lines.append('from handler import DiscoveryHandler, MonitoringHandler')
    lines.append('from discovery import HostDiscovery, VMDiscovery')
    lines.append('from monitoring import VMMonitoring,HostMonitoring')
    lines.append('def initialize_app():')
    lines.append('  Logger().setup_logger_config()')
    lines.append(
        '  Registery.RegisterHandlers({Constants.DISCOVERY_HANDLER_IDENTITY:DiscoveryHandler,Constants.MONITORING_HANDLER_IDENTITY:MonitoringHandler})')
    lines.append('  Registery.RegiterDiscoveryEntities([HostDiscovery,VMDiscovery])')
    lines.append('  Registery.RegisterMonitoringEntities({Constants.VM:VMMonitoring, Constants.HOST:HostMonitoring})')
    lines.append('  Init().start_server()')
    lines.append('if __name__ == "__main__":')
    lines.append('  initialize_app()')
    filename = os.getcwd()+"templates/app.py"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')