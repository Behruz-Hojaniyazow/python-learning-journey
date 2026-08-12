import unittest
from unittest.mock import Mock, MagicMock
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.mock_logger = Mock()
        self.calc = Calculator(self.mock_logger)
        
    def test_safe_divide_success(self):
        result = self.calc.safe_divide(10, 5)
        
        self.assertEqual(result, 2.0)
        self.mock_logger.error.assert_not_called()
        
    def test_safe_divide_by_zero(self):
        
        result = self.calc.safe_divide(10, 0)
        
        self.assertIsNone(result)
        self.mock_logger.error.assert_called_once_with('Division by zero attempted')
        
    def test_safe_divide_type_error(self):
        
        result = self.calc.safe_divide(10, 'abc')
        
        self.assertIsNone(result)
        self.mock_logger.error.assert_called_once_with('Invalid types for division')
        
    def test_safe_divide_unexpected_exception(self):
        
        mock_a = MagicMock()
        mock_a.__truediv__.side_effect = RuntimeError("Unexpected system failure")
        
        result = self.calc.safe_divide(mock_a, 5)
        
        self.assertIsNone(result)
        self.mock_logger.exception.assert_called_once_with('Unexpected error during division')
        
    def test_safe_divide_float_result(self):
        
        result = self.calc.safe_divide(7, 2)
        
        self.assertEqual(result, 3.5)
        self.mock_logger.error.assert_not_called()

if __name__ == "__main__":
    unittest.main()