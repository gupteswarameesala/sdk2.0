from logger import Logger
from main import start_server
from config import *

def initialize_app():
    Logger().setup_logger_config()
    Resources().load_vcenters()
    start_server()


if __name__ == "__main__":
    initialize_app()

