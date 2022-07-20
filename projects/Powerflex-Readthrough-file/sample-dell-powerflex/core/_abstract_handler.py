from ._requestcontext import RequestContext
from abc import *
import uuid

class AbstractHandler(ABC):
   
   def __init__(self, requestContext):
        self.requestContext = requestContext
    
   @abstractmethod
   def perform(self):
       pass

   def destroy(self):
        self.requestContext.destroy()
        self.requestContext = None
        
    