{% for key, value in native_type_dict.items() %}
from ._{{ key.title().replace(" ", "") }}_discovery import {{value}}Discovery
{% endfor %}