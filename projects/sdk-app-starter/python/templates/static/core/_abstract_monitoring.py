from abc import *

class AbstractMonitoring(ABC):
        
   @abstractmethod
   def monitor(requestContext):
       pass

  