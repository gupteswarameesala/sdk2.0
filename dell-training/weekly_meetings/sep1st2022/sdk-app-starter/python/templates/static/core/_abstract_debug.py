from abc import *


class AbstractDebug(ABC):

    @abstractmethod
    def debug(self, requestcontext):
        pass
