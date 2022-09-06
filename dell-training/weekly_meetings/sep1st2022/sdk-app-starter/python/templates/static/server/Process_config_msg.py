import threading
from core import Registery
import logging
from core import Constants

logger = logging.getLogger(__name__)


# Asynchronous task being performed
class ProcessConfigMsg(threading.Thread):

    def __init__(self, requestcontext):
        self.requestContext = requestcontext
        threading.Thread.__init__(self)

    # checking if the action need to perform is discovery or monitoring
    def run(self):
        handlerClass = Registery.getHandler(getHandlerIdentity(self.requestContext.get_request_data()["module"],
                                                               self.requestContext.get_request_data()["subtype"],
                                                               self.requestContext.get_request_data()["action"]))
        aa = handlerClass(self.requestContext)
        aa.perform()
        aa.destroy()


def getHandlerIdentity(module, subtype, action):
    return module + Constants.UNDERSCORE + subtype + Constants.UNDERSCORE + action
