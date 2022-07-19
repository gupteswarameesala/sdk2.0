import time

class Time:
    # Getting current time stamp
    def get_current_time(self):
        return str(int(time.time()))


class Constants:
    STATUS_OK = 200
    DISCOVERY = "DISCOVERY"
    MONITORING = "MONITORING"
    DISCOVERY_HANDLER_IDENTITY = "Discovery-Configuration-Update"
    MONITORING_HANDLER_IDENTITY = "Monitoring-Configuration-Update"

    DEVICE_REACHABILITY = "Device-Reachability"
   

