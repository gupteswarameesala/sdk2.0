from core import Constants, AbstractDiscovery
from httpclient import Url

import logging

logger = logging.getLogger(__name__)


class TargetDiscovery:
    {% for nt in nativeType %}

    def get_{{nt['name'].title().replace(" ", "")}}_data(self, requestContext,resource_type):
        pass
    {% endfor %}

