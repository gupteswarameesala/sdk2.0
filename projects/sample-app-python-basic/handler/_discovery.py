import logging
import time
from ._publisher import *

logger = logging.getLogger(__name__)

def discover(cloud_message, http_headers):
    payload = cloud_message.get("payload")
    data = payload.get('data')
    ip_add = data.get("ipAddress")
    port = data.get("port")
      
    logger.info("Ip Address:" + ip_add)
    logger.info("port:" + port)

    vcenter = discover_vcenter(http_headers)

    host = discover_host(vcenter, http_headers)

    discover_vm(host, http_headers)

    construct_app_event(http_headers, cloud_message)

    post_acknowledge(http_headers, "true")

def discover_vcenter(http_headers):
    vcenter_list = []
    vcenter = {
                'resourceType': 'Server', 
                'nativeType': 'vcenter',
                'moId': 'vCenter01', 
                'hasRelationship': 'true',
                'resourceName': 'vCenter01',
                'hostName': 'vCenter01',
                'ipAddress': '179.21.36.3'
              }

    http_headers['AM-App-Native-Type'] = "vcenter"

    vcenter_list.append(vcenter)

    publish_resources(http_headers, vcenter_list)

    return 'vCenter01'
 
def discover_host(vcenter, http_headers):
    host_list = []
    host = {
                'resourceType': 'Server', 
                'nativeType': 'host',
                'moId': 'Host01', 
                'hasRelationship': 'true',
                'resourceName': 'Host01',
                'hostName': 'Host01',
                'ipAddress': '179.21.36.4'
              }

    http_headers['AM-App-Native-Type'] = "host"

    host_list.append(host)

    publish_resources(http_headers, host_list)

    relationship_list = []
    vm01_relationship = {
                                'type': "componentOf", 
                                'sourceId': vcenter,
                                'targetId': 'Host01'
                            }
    relationship_list.append(vm01_relationship)

    publish_relationships(http_headers, relationship_list)

    return 'Host01'

def discover_vm(host, http_headers):
    vm_list = []
    vm01 = {
                'resourceType':'Server', 
                'nativeType': 'vm',
                'moId':'VM01',
                'hasRelationship':'true',
                'resourceName':'VM01',
                'hostName': 'VM01',
                'ipAddress': '179.21.36.5'
                }
    vm_list.append(vm01)

    vm02 = {
                'resourceType':'Server',
                'nativeType': 'vm',
                'moId': 'VM02',
                'hasRelationship': 'true',
                'resourceName': 'VM02',
                'hostName': 'VM02',
                'ipAddress': '179.21.36.6'
                 }
    
    vm_list.append(vm02)

    http_headers['AM-App-Native-Type'] = "vm"

    publish_resources(http_headers, vm_list)

    relationship_list = []
    vm01_relationship = {
                                'type': "componentOf", 
                                'sourceId': host,
                                'targetId': 'VM01'
                            }
    relationship_list.append(vm01_relationship)

    vm02_relationship = {
                                'type': 'componentOf',
                                'sourceId': host,
                                'targetId': 'VM02'
                             }
    relationship_list.append(vm02_relationship)

    publish_relationships(http_headers, relationship_list)

def construct_app_event(http_headers, cloud_message):
    event = {
                "version": "1.0.0",
                "id": "f92e909a-288b-4a17-bb55-1c4db3486925",
                "profile": cloud_message.get("gateway"),
                "gateway": cloud_message.get("gateway"),
                "app": cloud_message.get("app"),
                "collector": "GATEWAY",
                "appId": cloud_message.get("appIntegrationId"),
                "configId": cloud_message.get("configurationId"),
                "type": "LOG",
                "action": "POST",
                "payload": {
                    "message" : "Discovery completed successfully",
                    "statusCode" : "200",
                    "logLevel" : "INFO"
                },
                "timestamp": str(int(time.time()))
            }
    publish_app_event(http_headers, event)
    

     
