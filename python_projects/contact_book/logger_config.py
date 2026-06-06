import logging
from config import (
  LOG_FILE,
  LOGGER_NAME
)

def get_logger():
  """Create and return a configured logger instance."""

  # creating a log
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