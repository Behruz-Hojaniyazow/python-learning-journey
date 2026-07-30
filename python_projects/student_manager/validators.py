"""
Validation layer for the Kryos Student Manager System.

This module provides a single, cohesive collection of static validation
routines used to sanitize and verify raw, untrusted user input (always
received as strings from the console) before it is allowed to enter the
service layer or be persisted to storage.

Centralizing validation here — rather than scattering ``if`` checks
throughout the UI or service code — keeps the business rules (allowed
name characters, valid age/score ranges) in one auditable location and
guarantees that every entry point into the application enforces the same
rules consistently.

Each validator method returns a ``(bool, value_or_status)`` tuple:
    * On success: ``(True, <cleaned/converted value>)``.
    * On failure: ``(False, <StudentStatus member describing the failure>)``.

This convention allows calling code to use a single, uniform pattern —
``is_valid, result = StudentValidator.validate_x(...)`` — regardless of
which field is being validated.
"""

from config import (
    MAX_AGE,
    MIN_AGE,
    MAX_SCORE,
    MIN_SCORE
)
from status import StudentStatus

class StudentValidator:
    """A stateless collection of static validation rules for student data.

    This class is never instantiated; all of its methods are
    ``@staticmethod``s grouped together purely for namespacing and
    discoverability. Each method validates exactly one field of a
    student record (name, age, or score) in isolation, making the
    validators simple to unit-test and reuse independently of one
    another.
    """
    
    @staticmethod
    def validate_name(name: str) -> tuple[bool, StudentStatus | str]:
        """
        Validation functions for Student Manager.

        Cleans the raw name input (trimming surrounding whitespace and
        normalizing to lowercase) and verifies that, once internal
        spaces, hyphens, and apostrophes are stripped for the purpose of
        the check, the remaining characters are alphabetic only — i.e.
        the name contains no digits or symbols.

        Args:
            name (str): The raw, unvalidated name string as entered by
                the user.

        Returns:
            tuple[bool, str | StudentStatus]: A two-element tuple where
            the first element indicates whether validation succeeded.
            On success, the second element is the cleaned (trimmed,
            lowercased) name string. On failure, the second element is
            the :class:`StudentStatus` member describing the specific
            reason for failure — :attr:`StudentStatus.EMPTY_NAME` if the
            input was empty/whitespace-only, or
            :attr:`StudentStatus.INVALID_NAME_FORMAT` if it contains
            disallowed characters.
        """
        
        cleaned_name = name.strip().lower()
        if not cleaned_name:
            return False, StudentStatus.EMPTY_NAME
          
        allowed = cleaned_name.replace(" ", "").replace("-", "").replace("'", "")
        if not allowed.isalpha():
            return False, StudentStatus.INVALID_NAME_FORMAT
        return True, cleaned_name
        
    @staticmethod 
    def validate_age(age_str: str) -> tuple[bool, StudentStatus | int]:
        """
        Checking the student's age (Positive integer only)

        Validates that the provided age string is non-empty, represents
        a valid integer, and falls within the inclusive range defined by
        :data:`config.MIN_AGE` (exclusive lower bound) and
        :data:`config.MAX_AGE` (inclusive upper bound).

        Args:
            age_str (str): The raw, unvalidated age string as entered by
                the user.

        Returns:
            tuple[bool, int | StudentStatus]: A two-element tuple where
            the first element indicates whether validation succeeded.
            On success, the second element is the parsed integer age. On
            failure, the second element is the :class:`StudentStatus`
            member describing the specific reason for failure:
            :attr:`StudentStatus.EMPTY_AGE`,
            :attr:`StudentStatus.AGE_TOO_LOW`,
            :attr:`StudentStatus.AGE_TOO_HIGH`, or
            :attr:`StudentStatus.INVALID_AGE_FORMAT` (if the string
            cannot be parsed as an integer at all).
        """

        
        stripped_age = age_str.strip()
        if not stripped_age:
            return False, StudentStatus.EMPTY_AGE
          
        try:
            clean_age = int(stripped_age)
          
            if clean_age <= MIN_AGE:
                return False, StudentStatus.AGE_TOO_LOW
          
            if clean_age > MAX_AGE:
                return False, StudentStatus.AGE_TOO_HIGH
            return True, clean_age
        except ValueError:
            return False, StudentStatus.INVALID_AGE_FORMAT
    
    @staticmethod  
    def validate_score(score_str: str) -> tuple[bool, StudentStatus | int | float]:
        """
        Checking a student's exam score (a number from 0 to 100)

        Validates that the provided score string is non-empty,
        represents a valid numeric value, and falls within the inclusive
        range defined by :data:`config.MIN_SCORE` and
        :data:`config.MAX_SCORE`. Scores that are mathematically whole
        numbers (e.g. ``85.0``) are normalized to plain integers for
        cleaner downstream display and storage; genuinely fractional
        scores (e.g. ``85.5``) are preserved as floats.

        Args:
            score_str (str): The raw, unvalidated score string as
                entered by the user.

        Returns:
            tuple[bool, int | float | StudentStatus]: A two-element
            tuple where the first element indicates whether validation
            succeeded. On success, the second element is the parsed and
            normalized numeric score (``int`` if whole, ``float``
            otherwise). On failure, the second element is the
            :class:`StudentStatus` member describing the specific reason
            for failure: :attr:`StudentStatus.EMPTY_SCORE`,
            :attr:`StudentStatus.INVALID_SCORE_RANGE`, or
            :attr:`StudentStatus.INVALID_SCORE_FORMAT` (if the string
            cannot be parsed as a number at all).
        """
        
        stripped_score = score_str.strip()
        if not stripped_score:
            return False, StudentStatus.EMPTY_SCORE
            
        try:
            clean_score = float(stripped_score)
            
            if clean_score < MIN_SCORE or clean_score > MAX_SCORE:
                return False, StudentStatus.INVALID_SCORE_RANGE
              
            final_score = int(clean_score) if clean_score.is_integer() else clean_score
            return True, final_score
        except ValueError:
            return False, StudentStatus.INVALID_SCORE_FORMAT