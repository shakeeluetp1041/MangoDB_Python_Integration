import logging
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FOLDER_PATH = os.path.join(PROJECT_ROOT, 'logs')
def setup_logger(name, level=logging.WARNING):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    """Function to setup a logger with a specified name and log file."""
    log_file = os.path.join(LOG_FOLDER_PATH, f'{name}.log')
    
    # Ensure the logs directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if not logger.handlers:
        handler = logging.FileHandler(log_file, mode='w') # 'w' for overwrite, 'a' for append
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
if __name__ == "__main__":
    # Example usage
    logger = setup_logger('example_logger')
    logger.debug('This is debug message.')
    logger.info('This is an info message.')
    logger.error('This is an error message.')

