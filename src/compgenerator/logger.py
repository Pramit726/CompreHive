import logging
import os
from datetime import datetime


# Creating a log file name with current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating path for log file inside 'logs' directory
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Creating the directory for logs if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Creating full path for the log file
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configuring logging with specified settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Setting the log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Setting log message format
    level=logging.INFO,  # Setting logging level to INFO
)