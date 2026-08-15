"""
Unit tests for the StudentValidator module in the Kryos Student Manager System.

This test suite exhaustively verifies the static validation routines used to
sanitize and validate untrusted user input before processing. It ensures that
the `StudentValidator` enforces business rules (such as age limits, score ranges,
and name formatting) consistently and correctly.

The tests heavily utilize `unittest.TestCase.subTest` to parameterize test cases
and validate boundary conditions dynamically using the constraints defined in `config.py`.
"""

import unittest
from status import StudentStatus
from validators import StudentValidator
from config import (
    MAX_AGE, 
    MIN_AGE, 
    MAX_SCORE, 
    MIN_SCORE
)

class TestStudentValidator(unittest.TestCase):
    """
    Test suite for the StudentValidator class.

    Groups tests into three distinct validation areas:
    - Name validation: checks string formatting, alphabetic constraints, and normalization.
    - Age validation: ensures type safety and boundary checking for integer ages.
    - Score validation: validates numeric conversion (int vs. float) and strict ranges.
    """
    
    # ========================================================
    # PART-1, TEST VALIDATE NAME
    # ========================================================
    
    def test_validate_name_success(self):
        """
        Test successful validation of a standard, well-formatted name.
        Ensures the method returns True and lowercases the result.
        """
        
        name = "Behruz"
        
        is_valid, result = StudentValidator.validate_name(name)
        
        self.assertTrue(is_valid)
        self.assertEqual(result, "behruz")
        
    def test_validate_name_with_empty_spaces(self):
        """
        Test name validation with leading and trailing whitespaces.
        Ensures spaces are stripped correctly and the string is lowercased.
        """
        
        names_spaces = ["  beHruz ", "    mahMUt ", " anvAR "]
        
        for name in names_spaces:
            with self.subTest(name=name):
                
                is_valid, result = StudentValidator.validate_name(name)
                
                self.assertTrue(is_valid)
                self.assertEqual(result, name.strip().lower())
                
    def test_validate_name_with_signs(self):
        """
        Test name validation containing allowed internal characters.
        Ensures that names with internal spaces, hyphens, or apostrophes are
        accepted and appropriately normalized.
        """
        
        allowed_names = ["Behruz Hojaniyazow", "G'ayrat", "Mahmut-Hojaniyazow"]
        
        for name in allowed_names:
            with self.subTest(name=name):
                
                is_valid, result = StudentValidator.validate_name(name)
                
                self.assertTrue(is_valid)
                self.assertEqual(result, name.strip().lower())
                
    def test_validate_name_empty_names(self):
        """
        Test name validation with empty or whitespace-only strings.
        Ensures the method safely rejects these inputs and returns the EMPTY_NAME status.
        """
        
        empty_names = ["", " ", "\n", "\t", "\n\t", "\t\n"]
        
        for name in empty_names:
            with self.subTest(name=name):
                
                is_valid, result = StudentValidator.validate_name(name)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, StudentStatus.EMPTY_NAME)
                
    def test_validate_name_invalid_format(self):
        """
        Test name validation with disallowed characters.
        Ensures inputs containing digits or special symbols are rejected with
        the INVALID_NAME_FORMAT status.
        """
        
        invalid_names = ["Be#ruz", "123", "@nvar", "Mah_mut"]
        
        for name in invalid_names:
            with self.subTest(name=name):
                
                is_valid, result = StudentValidator.validate_name(name)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, StudentStatus.INVALID_NAME_FORMAT)
    
    # ========================================================
    # PART-2, TEST VALIDATE AGE
    # ========================================================
                
    def test_validate_age_success(self):
        """
        Test successful validation of valid age inputs.
        Dynamically checks ages well within the config-defined minimum and maximum boundaries.
        Ensures correct conversion to integer.
        """
        
        valid_ages = [str(MIN_AGE + 1), str(MAX_AGE), str((MAX_AGE + MIN_AGE) // 2)]
        
        for age in valid_ages:
            with self.subTest(age=age):
        
                is_valid, result = StudentValidator.validate_age(age)
                
                self.assertTrue(is_valid)
                self.assertEqual(result, int(age))
        
    def test_validate_age_empty_spaces(self):
        """
        Test age validation with surrounding whitespace.
        Ensures that otherwise valid age strings are parsed correctly despite spaces.
        """
        
        ages_spaces = [f"  {MAX_AGE-10}  ", f"  {MIN_AGE + 5} ", f"{MAX_AGE}  "]
        
        for age in ages_spaces:
            with self.subTest(age=age):
                
                is_valid, result = StudentValidator.validate_age(age)
                
                self.assertTrue(is_valid)
                self.assertEqual(result, int(age))
                
    def test_validate_age_empty_ages(self):
        """
        Test age validation with empty strings or pure whitespace.
        Ensures the method rejects them gracefully and returns the EMPTY_AGE status.
        """
        
        empty_ages = ["", " ", "\n", "\t", "\n\t", "\t\n"]
        
        for age in empty_ages:
            with self.subTest(age=age):
                
                is_valid, result = StudentValidator.validate_age(age)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, StudentStatus.EMPTY_AGE)
                
    def test_validate_age_too_low(self):
        """
        Test age validation for inputs strictly lower than or equal to MIN_AGE.
        Ensures rejection with the AGE_TOO_LOW status.
        """
        
        low_ages = [str(MIN_AGE), str(MIN_AGE - 5), str(MIN_AGE - 10)]
        
        for age in low_ages:
            with self.subTest(age=age):
                
                is_valid, result = StudentValidator.validate_age(age)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, StudentStatus.AGE_TOO_LOW)
                
    def test_validate_age_too_high(self):
        """
        Test age validation for inputs strictly exceeding MAX_AGE.
        Ensures rejection with the AGE_TOO_HIGH status.
        """
        
        high_ages = [str(MAX_AGE + 1), str(MAX_AGE + 5), str(MAX_AGE + 10)]
        
        for age in high_ages:
            with self.subTest(age=age):
                
                is_valid, result = StudentValidator.validate_age(age)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, StudentStatus.AGE_TOO_HIGH)
                
    def test_validate_age_invalid_format(self):
        """
        Test age validation with non-integer or malformed strings.
        Ensures floats, words, or improperly formatted numbers are rejected
        with the INVALID_AGE_FORMAT status.
        """
        
        invalid_ages = ["12,5", "4.6", "-6.6", "seven"]
        
        for age in invalid_ages:
            with self.subTest(age=age):
                
                is_valid, result = StudentValidator.validate_age(age)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, StudentStatus.INVALID_AGE_FORMAT)
                
    # ========================================================
    # PART-3, TEST VALIDATE SCORE
    # ========================================================
                
    def test_validate_score_success(self):
        """
        Test successful validation of valid exam scores within allowed boundaries.
        Critically verifies that scores equivalent to whole numbers are cast to integers,
        while fractional scores are preserved as floats.
        """
        
        allowed_scores = [
            (str(MAX_SCORE - 10), MAX_SCORE - 10, int),
            (str(MIN_SCORE + 30), MIN_SCORE + 30, int),
            ("95.4", 95.4, float),
            ("79.3", 79.3, float),
            ("85.0", 85, int)
        ]
        
        for score, expected_result, expected_type in allowed_scores:
            with self.subTest(score=score):
        
                is_valid, result = StudentValidator.validate_score(score)
                
                self.assertTrue(is_valid)
                self.assertEqual(result, expected_result)
                self.assertIsInstance(result, expected_type)
        
    def test_validate_score_white_spaces(self):
        """
        Test score validation with surrounding whitespace.
        Ensures valid numeric strings parse successfully even with padding.
        """
        
        scores_spaces = [f"  {MAX_SCORE - 30} ", f"{MIN_SCORE + 10}  ", f"   {MIN_SCORE}"]
        
        for score in scores_spaces:
            with self.subTest(score=score):
                
                is_valid, result = StudentValidator.validate_score(score)
                
                self.assertTrue(is_valid)
                self.assertEqual(result, int(score))
                
    def test_validate_score_empty_scores(self):
        """
        Test score validation with empty strings or pure whitespace.
        Ensures rejection with the EMPTY_SCORE status.
        """
        
        empty_scores = ['', ' ', '\n', '\t', '\n\t', '\t\n']
        
        for score in empty_scores:
            with self.subTest(score=score):
                
                is_valid, result = StudentValidator.validate_score(score)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, StudentStatus.EMPTY_SCORE)
                
    def test_validate_score_low_score(self):
        """
        Test score validation for inputs falling below MIN_SCORE.
        Ensures rejection with the INVALID_SCORE_RANGE status.
        """
        
        low_scores = [str(MIN_SCORE - 10), str(MIN_SCORE - 3.4), str(MIN_SCORE - 5.7)]
        
        for score in low_scores:
            with self.subTest(score=score):
                
                is_valid, result = StudentValidator.validate_score(score)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, StudentStatus.INVALID_SCORE_RANGE)
                
    def test_validate_score_high_scores(self):
        """
        Test score validation for inputs strictly exceeding MAX_SCORE.
        Ensures rejection with the INVALID_SCORE_RANGE status.
        """
        
        high_scores = [str(MAX_SCORE + 1), str(MAX_SCORE + 5), str(MAX_SCORE + 7.4)]
        
        for score in high_scores:
            with self.subTest(score=score):
                
                is_valid, result = StudentValidator.validate_score(score)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, StudentStatus.INVALID_SCORE_RANGE)
                
    def test_validate_score_invalid_format(self):
        """
        Test score validation with malformed or non-numeric string inputs.
        Ensures rejection with the INVALID_SCORE_FORMAT status.
        """
        
        invalid_scores = ['12,7', 'one', 'two']
        
        for score in invalid_scores:
            with self.subTest(score=score):
                
                is_valid, result = StudentValidator.validate_score(score)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, StudentStatus.INVALID_SCORE_FORMAT)
                
if __name__ == "__main__":
    unittest.main()