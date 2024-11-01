from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class AppLogger:
    @staticmethod
    def write_to_file(message):
        log_output = os.getenv('LOG_OUTPUT')
        with open(log_output, 'a') as file:
            file.write(message + "\n") 

    @staticmethod
    def debug(message):
        timestamp = datetime.now()
        log = f"{timestamp} - DEBUG: {message}"
        print(log)
        AppLogger.write_to_file(log)

    @staticmethod
    def info(message):
        timestamp = datetime.now()
        log = f"{timestamp} - INFO: {message}"
        print(log)
        AppLogger.write_to_file(log)

    @staticmethod
    def warning(message):
        timestamp = datetime.now()
        log = f"{timestamp} - WARNING: {message}"
        print(log)
        AppLogger.write_to_file(log)

    @staticmethod
    def error(message):
        timestamp = datetime.now()
        log = f"{timestamp} - ERROR: {message}"
        print(log)
        AppLogger.write_to_file(log)

    @staticmethod
    def critical(message):
        timestamp = datetime.now()
        log = f"{timestamp} - CRITICAL: {message}"
        print(log)
        AppLogger.write_to_file(log)

    @staticmethod
    def log(message, level='INFO'):
        if level == 'DEBUG':
            AppLogger.debug(message)
        elif level == 'INFO':
            AppLogger.info(message)
        elif level == 'WARNING':
            AppLogger.warning(message)
        elif level == 'ERROR':
            AppLogger.error(message)
        elif level == 'CRITICAL':
            AppLogger.critical(message)
