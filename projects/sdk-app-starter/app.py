import  sys
import os

from python import  *
from java import *
destination_path=sys.argv[1]
app_language = sys.argv[2]
current_path = os.getcwd()

def initialize_app_languge():
    #fun = getattr(self,"get_" + metric + "_data")(system_data)
    print(app_language + " app will be generted")
    if app_language == "java":
        initialize_java_app(destination_path, current_path)
    elif app_language == "python":
        initialize_python_app(destination_path,current_path)

if __name__ == "__main__":
    initialize_app_languge()

