from abc import *


class AbstractMonitoring(ABC):

    @abstractmethod
    def monitor(self, requestcontext):
        pass
