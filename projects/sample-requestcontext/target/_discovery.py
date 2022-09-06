import json

import requests
from .url import Url
from .constants import Constants

import logging

logger = logging.getLogger(__name__)


class TargetDiscovery:

    def get_Vcenter_data(self, requestContext, resource_type):
        rd = requestContext.context.get("app_data")
        data = rd.get('payload').get("data")
        ip_add = data.get("ipAddress")
        port = data.get("port")
        protocol = data.get("protocol")
        requestContext.context["base_url"] = self.construct_base_url(protocol, ip_add, port)
        vcenter_list = []
        #self.get_cipher(requestContext)
        relation_list = None
        vcenter_map = {'resourceType': resource_type, 'nativeType': 'vcenter',
                       'moId': data.get("vcenterName") + "@" + data.get("ipAddress"), "hasRelationship": "true",
                       'resourceName': data.get("vcenterName"),
                       'hostName': data.get("vcenterName"),
                       'ipAddress': data.get("ipAddress")}
        requestContext.context["root_moid"] = vcenter_map.get("moId")
        vcenter_list.append(vcenter_map)

        return vcenter_list, relation_list

    def get_Host_data(self, requestContext, resource_type):
        rd = requestContext.context.get("app_data")
        data = rd.get('payload').get("data")
        base_url = requestContext.context.get("base_url")
        vcenter_id = data.get("vcenterName")
        result = Url().discover_account(base_url, vcenter_id)
        print(result)
        requestContext.context["result"] = result
        hosts_list = []
        relation_list = []
        for host in result:
            logger.debug("Discovery started for host " + str(host['uuid']) + " with IPAddress" + str(host['ip']))
            hosts_map = {'resourceType': resource_type, 'nativeType': 'host', 'moId': host['uuid'],
                         'resourceName': host['name'], 'hostName': host['host'], 'ipAddress': host['ip'],
                         "hasRelationship": "true"}
            hosts_list.append(hosts_map)


            relation_map = {'type': "componentOf", 'sourceId': requestContext.context.get("root_moid"),
                            'targetId': host['uuid']}
            relation_list.append(relation_map)

        return hosts_list, relation_list

    def get_Vm_data(self, requestContext, resource_type):
        vms_list = []
        base_url = requestContext.context["base_url"]
        rd = requestContext.context.get("app_data")
        data = rd.get('payload').get("data")
        vcenter_id = data.get("vcenterName")
        result = Url().discover_account(base_url, vcenter_id)
        requestContext.context["result"] = result
        relation_list = []
        for host in result:
            for vm in host['vms']:
                logger.debug("Discovery started for vm " + str(vm['uuid']) + " with IPAddress" + str(vm['ip']))
                vm_map = {'resourceType': resource_type, 'nativeType': 'vm', 'moId': vm['uuid'],
                          "resourceName": vm['name'], 'hostName': vm['host'], 'ipAddress': vm['ip'],
                          "hasRelationship": "true"}
                vms_list.append(vm_map)

                relation_map = {'type': "componentOf", 'sourceId': host['uuid'],
                                'targetId': vm["uuid"]}
                relation_list.append(relation_map)

        return vms_list, relation_list

    def construct_base_url(self, server_protocol, server_address, server_port):
        return server_protocol + "://" + server_address + ":" + server_port + "/"

    def get_cipher(self, requestContext):
        if requestContext.context.get(Constants.DATA).get(Constants.CREDENTIAL) is not None:
            for cred in requestContext.context.get(Constants.DATA).get(Constants.CREDENTIAL):
                credobj = cred.get(Constants.CREDENTIALVALUE)
                if credobj is not None:
                    if cred.get(Constants.FIELDNAME) == Constants.CREDENTIALS and cred.get(Constants.FIELDNAME) is not None:
                        ciphertext = credobj.get(Constants.DATA).get(Constants.CIPHER)
                        key = credobj.get(Constants.DATA).get("key1")
                        res = self.get_credentials(ciphertext, key)
                        requestContext.context[Constants.USERNAME] = res.get(Constants.USERNAME)
                        requestContext.context[Constants.PASSWORD] = res.get(Constants.PASSWORD)
                        logger.info(
                            "username : " + str(requestContext.context[Constants.USERNAME]) + "     " + "password : " +
                            str(requestContext.context[Constants.PASSWORD]))
                else:
                    logger.info("Credential object not found")
        else:
            logger.info("NO credential object found")

    def get_credentials(self, cipher, key):
        url = "http://localhost:25001/api/v2/credentials/decrypt?key=" + key
        payload = cipher
        headers = {
            'Content-Type': 'text/plain'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        respon = json.loads(response.text)

        return respon


