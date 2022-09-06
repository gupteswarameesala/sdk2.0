import logging

logger = logging.getLogger(__name__)


class TargetDiscovery:
    {% for nt in nativeType %}
    def get_{{nt['name'].title().replace(" ", "").lower()}}_data(self, requestcontext, resource_type):
        pass
{% endfor %}
