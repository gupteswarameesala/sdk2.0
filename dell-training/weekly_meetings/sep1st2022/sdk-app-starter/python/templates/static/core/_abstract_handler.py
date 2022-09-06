from abc import *


class AbstractHandler(ABC):

    def __init__(self, requestcontext):
        self.requestcontext = requestcontext

    @abstractmethod
    def perform(self):
        pass

    def destroy(self):
        self.requestcontext.destroy()
        self.requestcontext = None
