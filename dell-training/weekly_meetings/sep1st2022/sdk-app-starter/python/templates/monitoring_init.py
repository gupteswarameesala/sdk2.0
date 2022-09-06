{% for key, value in native_type_dict.items() %}
from ._{{ key.title().replace(" ", "") }}_monitoring import {{value}}Monitoring
{% endfor %}
