from abc import *

class AbstractDiscovery(ABC):
        
   @abstractmethod
   def discover(requestContext):
       pass
