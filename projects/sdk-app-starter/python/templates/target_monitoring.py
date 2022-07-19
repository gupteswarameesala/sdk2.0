import datetime
import requests

from core import Time, Constants
from httpclient import Url
import logging

logger = logging.getLogger(__name__)

class TargetMonitoring:
    {% for nt in nativeType %}
    def process_{{nt['name'].title().replace(" ", "")}}_metrics(self, requestContext):
        pass

    {% endfor %}

