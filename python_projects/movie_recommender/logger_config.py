"""
Centralized logging configuration for the Movie Recommender application.

This module provides a single factory function, `get_logger`, that
constructs and configures the application-wide logger. It follows a
dual-handler strategy:

    - A `FileHandler` that persists ERROR and CRITICAL level messages
      (with detailed context: timestamp, filename, and line number) to
      a log file for post-mortem debugging.
    - A `StreamHandler` that prints INFO level and higher messages to
      the console, using a minimal format suitable for end users.

By funneling all logger creation through this single function, every
module in the application shares the same logger configuration,
preventing duplicate handlers and ensuring consistent log formatting
throughout the codebase.
"""

import logging
from config import (
  LOG_FILE,
  LOGGER_NAME,
  FILE_FORMAT,
  CONSOLE_FORMAT
)

def get_logger() -> logging.Logger:
    """
    Configure and return the application's shared logger instance.

    This function initializes (or retrieves, if already configured) a
    logger named according to `LOGGER_NAME`, sets its threshold to
    `DEBUG` so it can capture messages of any severity, and attaches
    two handlers:

    1. A `FileHandler` that writes only `ERROR` and `CRITICAL` messages
       to `LOG_FILE`, formatted with full diagnostic context
       (timestamp, logger name, filename, and line number) as defined
       by `FILE_FORMAT`.
    2. A `StreamHandler` (console) that writes `INFO` and higher
       messages to standard output, using the simplified format
       defined by `CONSOLE_FORMAT`.

    A guard clause checks `logger.handlers` before attaching new
    handlers, ensuring that calling this function multiple times
    (e.g., from different modules) does not result in duplicate log
    entries.

    Returns:
        logging.Logger: A fully configured, ready-to-use logger
        instance shared across the entire application.
    """

    
    # creating a log
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG) # Accepts logs of all level
    
    if not logger.handlers:
  
        # 1.Handler for writing to a file(ALL ERROR and CRITICAL ERRORS are written to a file for analysis)
        file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
        file_handler.setLevel(logging.ERROR)
        file_formatter = logging.Formatter(FILE_FORMAT)
        file_handler.setFormatter(file_formatter)
      
        # 2.Handler for output to the console (Only for the user or programmer can see on the screen)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(CONSOLE_FORMAT)
        console_handler.setFormatter(console_formatter)
      
        
        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger
