from server import start_server
from logger import configure_log

def initialize_app():
    configure_log()
    start_server()

if __name__ == "__main__":
    initialize_app()