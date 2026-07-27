"""
Status code definitions for the Movie Recommender application.

This module defines `MovieStatus`, a centralized enumeration of every
possible outcome that can be returned by the validation and service
layers throughout the application. Rather than returning raw booleans,
strings, or scattered error messages, every operation (adding,
searching, deleting, or recommending a movie) reports its result as a
`MovieStatus` member. The UI layer then maps each member to a
human-readable, user-facing message, keeping presentation concerns
fully decoupled from business logic.

By inheriting from `enum.Enum`, each member is a distinct, hashable,
comparable singleton exposing both `.name` (e.g., `"SUCCESS"`) and
`.value` (its underlying `auto()`-assigned integer). This allows the
rest of the codebase to safely call `status.name` when logging or
building fallback messages, and to use `MovieStatus` members directly
as dictionary keys (as done in `main.py`'s `ACTION_MESSAGES` and
`COMMON_ERRORS` mappings) with full confidence in correct, consistent
equality and hashing behavior.

Attributes:
    EMPTY_MOVIE: Returned when a submitted movie title is empty or
        contains only whitespace.
    DUPLICATE_MOVIE: Returned when the submitted movie already exists
        somewhere in the database.
    EMPTY_GENRE: Returned when a submitted genre name is empty or
        contains only whitespace.
    DUPLICATE_GENRE: Returned when the submitted genre already exists
        in the database.
    INVALID_CHOICE: Returned when a numeric menu selection falls
        outside the valid range of available options.
    INVALID_CHOICE_FORMAT: Returned when user input for a menu
        selection is not a valid digit string.
    SAVE_ERROR: Returned when an error occurs while persisting data to
        the underlying storage file.
    NOT_FOUND: Returned when a requested movie or genre cannot be
        located in the database.
    EMPTY_DATA: Returned when the movie database contains no data at
        all.
    SUCCESS: Returned when an operation completes without error.
"""

from enum import Enum, auto

class MovieStatus(Enum):
    """
    Enumeration of all outcome codes used across the application.

    Each member represents one specific, mutually exclusive result
    that a validation or service-layer operation can produce. Values
    are auto-assigned via `enum.auto()`; callers should never rely on
    the underlying integer value itself, only on member identity
    (e.g., `status == MovieStatus.SUCCESS`) or its `.name` attribute
    for logging and diagnostics.
    """

    EMPTY_MOVIE = auto()
    DUPLICATE_MOVIE = auto()
    EMPTY_GENRE = auto()
    DUPLICATE_GENRE = auto()
    INVALID_CHOICE = auto()
    INVALID_CHOICE_FORMAT = auto()
    SAVE_ERROR = auto()
    NOT_FOUND = auto()
    EMPTY_DATA = auto()
    SUCCESS = auto()