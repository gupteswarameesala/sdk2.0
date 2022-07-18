import datetime
import requests
from random import *
import os
import json
import time

from core import Time, Constants
from httpclient import Url
import logging

logger = logging.getLogger(__name__)

class TargetMonitoring:
    
    def process_Vcenter_metrics(self, requestContext):
        return self.process_metrics(requestContext)

    
    def process_Host_metrics(self, requestContext):
        return self.process_metrics(requestContext)

    
    def process_Vm_metrics(self, requestContext):
        return self.process_metrics(requestContext)


    def process_metrics(self, requestContext):
        
        payload = requestContext.context.get("app_data").get("payload")

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

        metrics_map_list = []
        for resourcesObject in resources:
            resourceId = resourcesObject.get("resourceId")
            moId = resourcesObject.get("moId")
         
            metric_map = {
                      'resourceId': resourceId, 
                      'resourceType': nativeType,
                      'templateId': templateId,
                      'monitorId': monitorId
                      }
            metrics_list = []
       
            for metric in metrics:
                if metric == "dell_demo_resource_event_statistics":
                    self.generate_alert(self.requestContext.context["http_headers"], requestContext.context.get("app_data"), resourceId, metric)
                    continue
                metrics = {'metricName': metric.replace(".","_"), 'instanceVal': str(randint(1, 100)), 'ts': str(int(time.time()))}
                metrics_list.append(metrics)

            metric_map['data'] = metrics_list

            metrics_map_list.append(metric_map)
       
        return metrics_map_list

    def generate_alert(self, http_headers, cloud_message, resourceId, metricName):

        random_number = randint(1, 100)
        currentState = None
        if random_number%2 == 0:
            currentState = "Ok"
        else:
            currentState = "Critical"

        alert = {
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

        self.publish_alerts(http_headers, alert)
    
    def publish_alerts(self, http_headers, alert):

        '''
        logger.info("Publish Alerts")
        logger.info(http_headers)
        logger.info(alert)
        logger.info(".....................")

        '''
        url = os.getenv('ADK_SERVICE_URI') + "/api/v2/messages/outbound_channel/publish"
        status_code = requests.post(url, json.dumps(alert), http_headers)
        logger.info(json.dumps(alert))
        if status_code == 200:
            logger.info("alerts posted" + str(alert))
        else:
            logger.info("Acknowledge posted failed.")
            logger.info(str(status_code))

    
