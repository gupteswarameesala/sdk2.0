import logging
import os
from core import Constants


# configuration to set up logger
class Logger:
    @staticmethod
    def setup_logger_config():
        log_level_env = os.getenv(Constants.LOG_LEVEL, Constants.INFO)
        if log_level_env == Constants.INFO:
            log_level = logging.INFO
        elif log_level_env == Constants.DEBUG:
            log_level = logging.DEBUG
        elif log_level_env == Constants.ERROR:
            log_level = logging.ERROR
        else:
            log_level = logging.INFO

        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=log_level)

    @staticmethod
    def modify_log_level(log_level_env):
        if log_level_env == Constants.INFO:
            log_level = logging.INFO
        elif log_level_env == Constants.DEBUG:
            log_level = logging.DEBUG
        elif log_level_env == Constants.ERROR:
            log_level = logging.ERROR
        else:
            log_level = logging.INFO

        logging.getLogger().setLevel(log_level)
