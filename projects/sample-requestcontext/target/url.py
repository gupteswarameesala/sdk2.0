import requests
import logging
import os
import time

logger = logging.getLogger(__name__)
base_adk_url = os.getenv('ADK_SERVICE_URI')


class Url:

    # Constructing the base url
    def construct_base_url(self, request_data):
        server_protocol = request_data.get('protocol')
        server_address = request_data.get('ipAddress')
        server_port = request_data.get('port')
        url = server_protocol + "://" + server_address + ":" + server_port + "/"
        return url

    # Constructing target device url
    def host_url(self, base_url, vcenterid):
        url = base_url + "api/v1/vcenters/" + vcenterid + "/" + "hosts"
        return url

    # Constructing hosts metrics url
    def host_metrics_url(self, base_url, vcenter_id, host_id):
        url = base_url + "api/v1/vcenters/" + vcenter_id + "/hosts/" + host_id + "/metrics"
        return url

    # Constructing vms metrics url
    def vm_metrics_url(self, base_url, vcenter_id, host_id):
        url = base_url + "api/v1/vcenters/" + vcenter_id + "/hosts/" + host_id + "/vms/metrics"
        return url

    def discover_account(self, base_url, vcenter_id):
        try:
            url = base_url + "api/v1/vcenters/" + vcenter_id + "/" + "hosts"
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            raise Exception(str(e))

    def alerts_url(self, base_url):
        url = base_url + "api/v1/types/alert/instances"
        return url





