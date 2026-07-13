"""
Logging configuration for the Contact Book application.

This module creates and configures the application's central
logger with both file and console handlers.

The logger records important application events, warnings,
errors, and critical exceptions, providing reliable diagnostics
for debugging and maintenance.
"""

import logging
from config import (
  LOG_FILE,
  LOGGER_NAME
)

def get_logger():
    """
    Create, configure, and return the application's logger instance.

    This function initializes the project's central logger and
    configures two logging handlers:

    1. A file handler that records only ERROR and CRITICAL log
       messages for long-term storage and debugging purposes.

    2. A console handler that displays INFO and higher-level log
       messages to provide real-time feedback during program
       execution.

    The logger is configured only once. If handlers have already
    been attached, the existing logger instance is returned to
    prevent duplicate log entries caused by multiple handlers.

    Logging Configuration:
        - Logger Level:
            DEBUG

        - File Handler:
            Records ERROR and CRITICAL messages.

        - Console Handler:
            Displays INFO, WARNING, ERROR, and CRITICAL messages.

        - Log File Encoding:
            UTF-8

    Returns:
        logging.Logger:
            A fully configured logger instance ready for use
            throughout the application.
    """

    # Create the application's logger instance.
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG) # Accepts logs of all levels
  
    # 1.Handler for writing to a file(ALL ERROR and CRITICAL ERRORS are written to a file for analysis)
    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setLevel(logging.ERROR)
    file_formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s [%(name)s:%(filename)s:%(lineno)d] - %(message)s'
    )
    file_handler.setFormatter(file_formatter)
  
    # 2.Handler for output to the console (Only for the user or programmer can see on the screen)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)
  
    if not logger.handlers:
        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger