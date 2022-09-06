import datetime
import os

import requests

from core import Time, Constants, GatewayToCloudMessage
from httpclient import Url
from .url import Url
import logging
from .constants import Constants

logger = logging.getLogger(__name__)

env_metric = os.getenv("METRIC","dell_demo")  # number of hosts


class TargetMonitoring:

    def process_Vcenter_metrics(self, requestContext):
        metric_list = []
        for resourcesObject in requestContext.context.get("resources"):
            # resourcesObject = resource.get(Constants.RESOURCES)
            resourceId = resourcesObject.get("resourceId")
            moId = resourcesObject.get("moId")
            metrics = requestContext.context.get("metrics")
            metrics_list = []
            data = requestContext.context.get("data")
            ip_add = data.get("ipAddress")
            port = data.get("port")
            protocol = data.get("protocol")
            requestContext.context["base_url"] = self.construct_base_url(protocol, ip_add, port)
            url = Url().alerts_url(requestContext.context.get("base_url"))
            response = requests.get(url)
            if response.status_code == Constants.STATUS_OK:
                alert_data = response.json()
                for metric in metrics:
                    if metric == env_metric + "_" + "resource_event_statistics":
                        metrics = self.get_alert_metrics(requestContext, resourceId, alert_data, metric, moId)
                        for metric in metrics:
                            metrics_list.append(metric)
            else:
                logger.info("Failed to get metrics")
                logger.info(response.reason)
        if metrics_list != None and len(metrics_list)>0:
            for metric in metrics_list:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "vcenter"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_alerts(requestContext.context.get("http_headers"), metric)
        return None

    def get_alert_metrics(self, requestContext, resourceId, result, metric, moid):
        metric_list = self.create_alert_metrics(requestContext, resourceId, result, metric, moid)
        return metric_list

    def create_alert_metrics(self, requestContext, resourceId, result, metric, moid):

        metrics_list = []
        for res in result:
            metrics = {
                "version": requestContext.context.get("app_data").get("appVersion"),
                "id": "",
                "app": requestContext.context.get("app_data").get("app"),
                "appId": requestContext.context.get("app_data").get("appIntegrationId"),
                "configId": requestContext.context.get("app_data").get("configurationId"),
                "module": "",
                "type": "ALERT",
                "subType": "",
                "action": "POST",
                "payload": {
                    "resourceId": resourceId,
                    "uuId": moid,
                    "alertType": "Monitoring",
                    "serviceName": res.get("eventName"),
                    "subject": self.getKeys(res.get("eventType")) + " - " + res.get("eventName"),
                    "description": res.get("eventDescription") + " On " + res.get("eventOn"),
                    "currentState": self.getKeys(res.get("eventType")),
                    "alertTime": res.get("eventTime")
                }
            }
            metrics_list.append(metrics)
        return metrics_list

    def process_Host_metrics(self, requestContext):
        metrics_list = []
        for resourcesObject in requestContext.context.get("resources"):
            # resourcePayload = resource.get('payload')
            # resourcesObject = resource.get('resources')
            resourceId = resourcesObject.get("resourceId")
            host_id = resourcesObject.get("moId").split("@", 1)[1]

            data = requestContext.context.get("data")
            ip_add = data.get("ipAddress")
            port = data.get("port")
            protocol = data.get("protocol")
            requestContext.context["base_url"] = self.construct_base_url(protocol, ip_add, port)

            url = Url().host_metrics_url(requestContext.context.get("base_url"),
                                         requestContext.context.get("data").get("vcenterName"), host_id)
            response = requests.get(url)
            if response.status_code == Constants.STATUS_OK:
                result = response.json()
                metrics = self.get_host_metrics(requestContext, resourceId, result)
                # print(metrics)
                for metric in metrics:
                    metrics_list.append(metric)
                logger.debug("completed processing of " + str(host_id))
            else:
                logger.info("Failed to get metrics")
                logger.info(response.reason)
        return metrics_list

    def get_host_metrics(self, requestContext, resourceId, result):
        metric_list = []
        metric_map = self.create_host_metrics(requestContext, resourceId, result)
        metric_list.append(metric_map)
        return metric_list

    def create_host_metrics(self, requestContext, resourceId, result):
        metric_map = {'resourceId': resourceId, 'resourceType': requestContext.context.get("nativeType"),
                      'templateId': requestContext.context.get("templateId"),
                      'monitorId': requestContext.context.get("monitorId")}
        metrics_list = []
        for res in result:

            newMetricName = str(env_metric) + "_host_" + res['name'].replace(".", "_")
            metrics = {'metricName': newMetricName, 'instanceVal': str(res['value']), 'ts': Time().get_current_time()}
            metrics_list.append(metrics)
        metric_map['data'] = metrics_list
        return metric_map

    def process_Vm_metrics(self, requestContext):
        metrics_list = []
        for resourcesObject in requestContext.context.get("resources"):
            # resourcePayload = resource.get('payload')
            # print("payload "+ resourcePayload)
            # resourcesObject = resource.get('resources')
            resourceId = resourcesObject.get("resourceId")
            host_id = resourcesObject.get("moId").split("@", 2)[1]
            VM_Name = resourcesObject.get("moId").split("@", 2)[2]
            VM_Id = resourcesObject.get("moId").split("@", 2)[0] + resourcesObject.get("moId").split("@", 2)[1] + \
                    resourcesObject.get("moId").split("@", 2)[2]

            data = requestContext.context.get("data")
            ip_add = data.get("ipAddress")
            port = data.get("port")
            protocol = data.get("protocol")
            requestContext.context["base_url"] = self.construct_base_url(protocol, ip_add, port)

            url = Url().vm_metrics_url(requestContext.context.get("base_url"),
                                       requestContext.context.get("data").get("vcenterName"), host_id)
            response = requests.get(url)
            if response.status_code == Constants.STATUS_OK:
                result = response.json()
                metrics = self.get_vm_metrics(requestContext, result, resourceId, VM_Id)
                metrics_list.append(metrics)
                logger.debug("completed processing of " + str(host_id) + str(VM_Name))
        return metrics_list

    def get_vm_metrics(self, requestContext, result, resourceId, vmId):
        metric_list = []
        for i in result:
            for key, value in i.items():
                if key == vmId:
                    # logger.info("Iterating metric list for key  " + key)
                    metric_list = self.create_vm_metrics(requestContext, resourceId, value)
                    return metric_list

        # Constructing the metrics of the resources

    def create_vm_metrics(self, requestContext, resourceId, result):
        metric_map = {'resourceId': resourceId, 'resourceType': requestContext.context.get("nativeType"),
                      'templateId': requestContext.context.get("templateId"),
                      'monitorId': requestContext.context.get("monitorId")}
        metrics_list = []
        for res in result:
            newMetricName = str(env_metric) + "_vm_" + res['name'].replace(".", "_")
            metrics = {'metricName': newMetricName, 'instanceVal': str(res['value']), 'ts': Time().get_current_time()}
            metrics_list.append(metrics)
        metric_map['data'] = metrics_list
        return metric_map

    def construct_base_url(self, server_protocol, server_address, server_port):
        return server_protocol + "://" + server_address + ":" + server_port + "/"

    def getKeys(self, key):
        switcher = {
            "Information": "Ok",
            "Audit": "Ok",
            "Error": "Critical"

        }
        return switcher.get(key, "")






