import logging

logger = logging.getLogger(__name__)


class TargetMonitoring:
    {% for nt in nativeType %}
    def process_{{nt['name'].title().replace(" ", "").lower()}}_metrics(self, requestcontext):
        pass
{% endfor %}