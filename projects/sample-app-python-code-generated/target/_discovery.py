from core import Constants, AbstractDiscovery
from httpclient import Url

import logging

logger = logging.getLogger(__name__)


class TargetDiscovery:
    

    def get_Vcenter_data(self, requestContext,resource_type):
        vcenter_list = []
        vcenter = {
                'resourceType': resource_type, 
                'nativeType': 'vcenter',
                'moId': 'vCenter01', 
                'hasRelationship': 'true',
                'resourceName': 'vCenter01',
                'hostName': 'vCenter01',
                'ipAddress': '179.21.36.3'
              }
        vcenter_list.append(vcenter)
        requestContext.context["root_moid"] = 'vCenter01'
        return vcenter_list, None

    def get_Host_data(self, requestContext,resource_type):
        host_list = []
        host = {
                'resourceType': resource_type, 
                'nativeType': 'host',
                'moId': 'Host01', 
                'hasRelationship': 'true',
                'resourceName': 'Host01',
                'hostName': 'Host01',
                'ipAddress': '179.21.36.4'
              }

        host_list.append(host)

        relationship_list = []
        vm01_relationship = {                              
                                'type': "componentOf", 
                                'sourceId': requestContext.context.get("root_moid"),
                                'targetId': 'Host01'
                            }
        relationship_list.append(vm01_relationship)

        requestContext.context["host_moid"] = 'Host01'

        return host_list, relationship_list

            
    def get_Vm_data(self, requestContext,resource_type):
        vm_list = []
        vm01 = {
                'resourceType':resource_type, 
                'nativeType': 'vm',
                'moId':'VM01',
                'hasRelationship':'true',
                'resourceName':'VM01',
                'hostName': 'VM01',
                'ipAddress': '179.21.36.5'
                }
        vm_list.append(vm01)

        vm02 = {
                'resourceType':resource_type,
                'nativeType': 'vm',
                'moId': 'VM02',
                'hasRelationship': 'true',
                'resourceName': 'VM02',
                'hostName': 'VM02',
                'ipAddress': '179.21.36.6'
                 }
    
        vm_list.append(vm02)

    
        relationship_list = []
        vm01_relationship = {
                                'type': "componentOf", 
                                'sourceId': requestContext.context.get("host_moid"),
                                'targetId': 'VM01'
                            }
        
        relationship_list.append(vm01_relationship)
    
        vm02_relationship = {
                                'type': "componentOf", 
                                'sourceId': requestContext.context.get("host_moid"),
                                'targetId': 'VM02'
                            }
        relationship_list.append(vm02_relationship)
        
        return vm_list, relationship_list
    
