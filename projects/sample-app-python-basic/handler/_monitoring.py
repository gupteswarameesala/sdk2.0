import logging
import time
from random import *
from ._publisher import *

logger = logging.getLogger(__name__)

def monitor(cloud_message, http_headers):
    payload = cloud_message.get("payload")

    templateId = payload["templateId"]
    monitorId = payload["monitorId"]

    appConfig = payload.get('appConfig')
    data = appConfig.get('data')

    ip_add = data.get("ipAddress")
    port = data.get("port") 

    logger.info("IP Address:"+ ip_add)
    logger.info("Port:"+ port)
         
    nativeType = None
    for nativeTypeKey in payload["nativeType"].keys():
        nativeType = nativeTypeKey
    
    metrics = payload.get("nativeType").get(list(payload.get("nativeType").keys())[0])
    
    resources = payload.get('resources')


    for resourcesObject in resources:
        resourceId = resourcesObject.get("resourceId")
        moId = resourcesObject.get("moId")

        metrics_map_list = []

        metric_map = {
                      'resourceId': resourceId, 
                      'resourceType': nativeType,
                      'templateId': templateId,
                      'monitorId': monitorId
                      }
        metrics_list = []
       
        for metric in metrics:
            if metric == "dell_demo_resource_event_statistics":
                generate_alert(http_headers, cloud_message, resourceId, metric)
                continue
            metrics = {'metricName': metric.replace(".","_"), 'instanceVal': str(randint(1, 100)), 'ts': str(int(time.time()))}
            metrics_list.append(metrics)

        metric_map['data'] = metrics_list

        metrics_map_list.append(metric_map)

        publish_metrics(http_headers,metrics_map_list)
    
    post_acknowledge(http_headers, "false")


def generate_alert(http_headers, cloud_message, resourceId, metricName):

    random_number = randint(1, 100)
    currentState = None
    if random_number%2 == 0:
       currentState = "Ok"
    else:
       currentState = "Critical"

    metrics = {
                "version": "1.0.0",
                "id": "",
                "app": cloud_message.get("app"),
                "appId": cloud_message.get("appIntegrationId"),
                "configId": cloud_message.get("configurationId"),
                "module": "",
                "type": "ALERT",
                "subType": "",
                "action": "POST",
                "payload": {
                    "resourceId": resourceId,
                    "alertType": "Monitoring",
                    "serviceName": metricName,
                    "subject": "sample app target event processed as alert",
                    "description": "sample app target event processed as alert",
                    "currentState": currentState,
                    "alertTime": str(int(time.time()))
                }
            }

    publish_alerts(http_headers, metrics)
        
