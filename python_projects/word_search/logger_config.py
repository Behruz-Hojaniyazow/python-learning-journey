import logging
from config import (
  LOGGER_NAME,
  LOG_FILE
)

def get_logger():
  """
  Configures and returns a professional logger instance.
  
  This function initializes a logger with a DEBUG threshold and sets up two handlers:
  1. A FileHandler that records ERROR and CRITICAL messages with detailed contextual info.
  2. A StreamHandler (Console) that outputs INFO and higher messages with clean formatting.
  
  It safely checks for existing handlers to prevent duplicate log entries.
  
  Returns:
    logging.Logger: A fully configured logger instance ready for application-wide use.
  """
  
  # creating a log
  logger = logging.getLogger(LOGGER_NAME)
  logger.setLevel(logging.DEBUG) # Accepts logs of all level
  logger.propagate = False
  
  # 1.Handler for writing to a file (ALL ERROR and CRITICAL ERRORS are written to a file for analysis)
  file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
  file_handler.setLevel(logging.ERROR)
  file_formatter = logging.Formatter(
    "[%asctime)s] %(levelname)s [%(name)s:%(filename)s:%(lineno)d] - %(message)s", datefmt = "%Y-%m-%d %H:%M:%S"
  )
  file_handler.setFormatter(file_formatter)
  
  # 2.Handler for output to the console (Only for the user or programmer can see on the screen)
  console_handler = logging.StreamHandler()
  console_handler.setLevel(logging.INFO)
  console_formatter = logging.Formatter("%(levelname)s: %(message)s")
  console_handler.setFormatter(console_formatter)
  
  if not logger.handlers:
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
  return logger