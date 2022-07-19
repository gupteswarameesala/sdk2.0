from abc import *

class AbstractDebug(ABC):
        
   @abstractmethod
   def debug(requestContext):
       pass