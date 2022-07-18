import logging
from ._discovery import discover
from ._monitoring import monitor

logger = logging.getLogger(__name__)

def process_message(cloud_message, http_headers):
    module = cloud_message['module']
    if module == "Discovery":
        discover(cloud_message, http_headers)
    elif module == "Monitoring":
        monitor(cloud_message, http_headers)
        



