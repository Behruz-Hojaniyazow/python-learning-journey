"""
Logger configuration module for the Kryos Student Manager System.

This module is responsible for constructing and configuring a single,
application-wide ``logging.Logger`` instance. It follows the standard
"dual-handler" logging pattern:

    1. A :class:`logging.FileHandler` that persists ERROR and CRITICAL
       level records to a log file for post-mortem analysis and auditing.
    2. A :class:`logging.StreamHandler` that surfaces all log levels
       (DEBUG and above) directly to the console for real-time visibility
       during development and interactive use.

All formatting and destination settings are sourced from :mod:`config`,
ensuring that logging behavior can be adjusted without touching this
module's logic.

Typical usage example:
    >>> from logger_config import get_logger
    >>> logger = get_logger()
    >>> logger.error("Something went wrong while saving the record.")
"""

import logging
from config import (
  LOGGER_NAME,
  LOG_FILE,
  FILE_FORMAT,
  CONSOLE_FORMAT
)

def get_logger():
    """Create, configure, and return the application's shared logger.

    This function implements a singleton-like retrieval pattern: it fetches
    the logger registered under :data:`config.LOGGER_NAME` via
    ``logging.getLogger``, which guarantees that repeated calls across
    different modules return the *same* underlying logger instance rather
    than creating duplicates.

    Handler registration is guarded by an ``if not logger.handlers`` check
    to prevent duplicate handlers (and therefore duplicate log output)
    being attached if this function is called multiple times during the
    application's lifetime.

    The logger is configured with two handlers:
        * **File handler** — level ``ERROR`` and above, formatted with
          :data:`config.FILE_FORMAT` (includes timestamp, logger name,
          source file, and line number) and written to
          :data:`config.LOG_FILE` using UTF-8 encoding.
        * **Console handler** — level ``DEBUG`` and above, formatted with
          :data:`config.CONSOLE_FORMAT` (a concise level + message format)
          for readable, real-time terminal output.

    Returns:
        logging.Logger: A fully configured logger instance, set to accept
        all severity levels (``DEBUG`` and above) at the logger level,
        with per-handler level filtering applied as described above.
    """
    
    # creating a log
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG) # Accepts logs of all levels
    
    if not logger.handlers:
        
        # 1.Handler for writing to a file (All ERROR and CRITICAL ERRORS are written to a file for analysis)
        file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
        file_handler.setLevel(logging.ERROR)
        file_formatter = logging.Formatter(FILE_FORMAT)
        file_handler.setFormatter(file_formatter)
      
        # 2.Handler for output to the console (Only for the user or programmer can see on the screen)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter(CONSOLE_FORMAT)
        console_handler.setFormatter(console_formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger