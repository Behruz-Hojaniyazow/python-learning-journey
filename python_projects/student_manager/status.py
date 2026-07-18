"""
Status definitions module for the Kryos Student Manager System.

This module defines a single source of truth for every possible outcome
that can result from an operation performed on a student record (creation,
validation, search, or deletion). By representing outcomes as members of
an :class:`enum.Enum` rather than raw strings, integers, or booleans, the
codebase gains:

    * **Type safety** — invalid or misspelled status values are caught at
      development time rather than causing silent bugs at runtime.
    * **Decoupling** — business logic (in ``student_service.py`` and
      ``validators.py``) can return a status without needing to know how
      that status will ultimately be displayed to the user.
    * **Maintainability** — user-facing messages associated with each
      status are mapped separately (see ``main.py``), so wording can be
      changed without touching the underlying logic.
"""

from enum import Enum, auto

class StudentStatus(Enum):
    """Enumerates all possible result states for student-related operations.

    Each member represents a distinct outcome that can be returned by the
    service and validation layers after attempting to add, update, search
    for, or delete a student record. Values are auto-generated via
    :func:`enum.auto` since only the symbolic name (not the underlying
    integer value) is ever relied upon by the rest of the application.

    Attributes:
        SUCCESS: The requested operation completed successfully.
        SAVE_ERROR: A system-level failure occurred while persisting data
            to storage (e.g. an I/O or serialization error).
        EMPTY_NAME: The provided student name was empty or whitespace-only.
        DUPLICATE_NAME: A student with the same name already exists in the
            class register.
        EMPTY_AGE: The provided age field was empty or whitespace-only.
        EMPTY_SCORE: The provided score field was empty or whitespace-only.
        AGE_TOO_LOW: The provided age is below the configured minimum
            (see :data:`config.MIN_AGE`).
        AGE_TOO_HIGH: The provided age exceeds the configured maximum
            (see :data:`config.MAX_AGE`).
        INVALID_SCORE_FORMAT: The provided score is not a valid numeric
            value.
        INVALID_NAME_FORMAT: The provided name contains characters other
            than letters.
        INVALID_AGE_FORMAT: The provided age is not a valid numeric value.
        INVALID_SCORE_RANGE: The provided score falls outside the
            configured valid range (see :data:`config.MIN_SCORE` and
            :data:`config.MAX_SCORE`).
        NOT_FOUND: No student matching the given search criteria could be
            found in the class register.
    """
    
    SUCCESS = auto()
    SAVE_ERROR = auto()
    EMPTY_NAME = auto()
    DUPLICATE_NAME = auto()
    EMPTY_AGE = auto()
    EMPTY_SCORE = auto()
    AGE_TOO_LOW = auto()
    AGE_TOO_HIGH = auto()
    INVALID_SCORE_FORMAT = auto()
    INVALID_NAME_FORMAT = auto()
    INVALID_AGE_FORMAT = auto()
    INVALID_SCORE_RANGE = auto()
    NOT_FOUND = auto()