"""
Configuration module for the Movie Recommender application.

This module centralizes all static configuration values used across the
application, including the file path used for persisting movie data, the
file path used for application logs, the logger's identifying name, and
the formatting templates applied to both file-based and console-based
log output.

Centralizing these constants in a single module ensures consistency
across the codebase and simplifies future maintenance — for example,
changing the storage file name or adjusting the log format only
requires a single edit here, rather than hunting through multiple
modules.

Attributes:
    FILE_NAME (str): Path to the JSON file used to persist the movie
        database (genres and their associated movie lists).
    LOG_FILE (str): Path to the log file where ERROR and CRITICAL level
        messages are written for later diagnostics.
    LOGGER_NAME (str): The name used to identify the application's logger
        instance, retrieved via `logging.getLogger(LOGGER_NAME)`.
    FILE_FORMAT (str): The logging format string used by the file handler.
        Includes timestamp, log level, logger name, source filename, line
        number, and the log message — intended for detailed debugging.
    CONSOLE_FORMAT (str): The logging format string used by the console
        handler. Includes only the log level and message, intended for
        clean, user-facing output.
"""


FILE_NAME = "movies.json"
LOG_FILE = "movies_app.log"
LOGGER_NAME = "MovieRecommender"
FILE_FORMAT = "[%(asctime)s] %(levelname)s [%(name)s:%(filename)s:%(lineno)d] - %(message)s"
CONSOLE_FORMAT = "%(levelname)s: %(message)s"