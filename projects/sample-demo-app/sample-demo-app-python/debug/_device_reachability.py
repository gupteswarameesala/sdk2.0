from core import AbstractDebug, Constants
import logging
import requests

logger = logging.getLogger(__name__)

class DeviceReachability(AbstractDebug):

    def debug(self, requestContext):
        try:
              rd = requestContext.get_request_data()
              payload = rd.get('payload')
              vcenter_id = payload.get('vcenterName')
              requestContext.context["vCenterName"] = vcenter_id

              base_url = self.construct_base_url(payload.get('protocol'), payload.get('ipAddress'), payload.get('port'))
              status_code = self.discover_account(base_url, vcenter_id)
              if status_code == Constants.STATUS_OK:
                 return "Device reachable"
              else:
                 return "Device not reachable"
        except Exception as e:
              #raise Exception(str(e))
              return "Device not rechable"
      
    def discover_account(self, base_url, vcenter_id):
        try:
            url = base_url + "api/v1/vcenters/" + vcenter_id + "/" + "hosts"
            response = requests.get(url)
            return response.status_code
        except Exception as e:
            raise Exception(str(e))
    
    def construct_base_url(self, server_protocol, server_address, server_port):
        return server_protocol + "://" + server_address + ":" + server_port + "/"