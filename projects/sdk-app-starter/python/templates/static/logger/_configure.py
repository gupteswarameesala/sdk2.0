import logging
import os


# configuration to set up logger
class Logger:
    def setup_logger_config(self):
        log_level_env = os.getenv('LOG_LEVEL', 'INFO')
        if log_level_env == "INFO":
            log_level = logging.INFO
        elif log_level_env == "DEBUG":
            log_level = logging.DEBUG
        elif log_level_env == "ERROR":
            log_level = logging.ERROR
        else:
            log_level = logging.INFO

        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=log_level)
    
    def modify_log_level(self, log_level_env):
        log_level = logging.INFO
        if log_level_env == "INFO":
            log_level = logging.INFO
        elif log_level_env == "DEBUG":
            log_level = logging.DEBUG
        elif log_level_env == "ERROR":
            log_level = logging.ERROR
        else:
            log_level = logging.INFO
        
        logging.getLogger().setLevel(log_level)

        
