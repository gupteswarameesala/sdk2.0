import logging

def configure_log():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def modify_log_level(log_level_env):
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