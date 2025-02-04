

class RequestContext:

    def __init__(self, uuid, request_data):
        self.uuid = uuid
        self.request_data = request_data
        self.context = {}

    def get_request_data(self):
        return self.request_data

    def get_context(self):
        return self.context

    def set_context(self, context):
        self.context = context

    def destroy(self):
        self.uuid = None
        self.request_data = None
        self.context = None
