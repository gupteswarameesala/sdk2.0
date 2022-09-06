from abc import *


class AbstractDiscovery(ABC):

    @abstractmethod
    def discover(self, requestcontext):
        pass
