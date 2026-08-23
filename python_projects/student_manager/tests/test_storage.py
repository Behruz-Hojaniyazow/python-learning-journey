"""
Unit tests for the JSONStudentStorage persistence layer.

The test suite isolates filesystem access and logging with unittest.mock
and verifies successful operations together with expected storage failures.
"""

import unittest
import json
from storage import JSONStudentStorage
from unittest.mock import patch, mock_open

class TestJSONStudentStorage(unittest.TestCase):
    """Test JSONStudentStorage file operations and failure handling."""
    
    def setUp(self) -> None:
        """Create the storage instance and isolate the application logger."""
        
        # Mock the application logger for isolated logging tests.
        self.logger_patcher = patch("storage.get_logger")
        self.mock_get_logger = self.logger_patcher.start()
        self.mock_logger = self.mock_get_logger.return_value
        
        # Shared test fixtures.
        self.file_name = "test_students.json"
        self.storage = JSONStudentStorage(self.file_name)
        self.sample_students = [{'name': 'behruz', 'age': 18, 'score': 98}]
        self.sample_json_str = json.dumps(self.sample_students)
        
    def tearDown(self) -> None:
        """Stop the logger patcher after each test."""
        
        self.logger_patcher.stop()
     
    @patch('builtins.open', new_callable=mock_open)   
    def test_load_students_success(self, mock_file) -> None:
        """Return persisted students when the JSON file is valid."""
        
        mock_file.return_value.read.return_value = self.sample_json_str
        
        result = self.storage.load_students()
        
        self.assertEqual(result, self.sample_students)
        
        mock_file.assert_called_once_with(self.file_name, 'r', encoding='utf-8')
    
    @patch('builtins.open', side_effect=FileNotFoundError)    
    def test_load_students_file_not_found(self, mock_file) -> None:
        """Return an empty list and log at debug level when the file is missing."""
        
        result = self.storage.load_students()
        
        self.assertEqual(result, [])
        self.mock_logger.debug.assert_called_once_with(
            f"'{self.file_name}' not found, returned an empty list"
        )
    
    @patch('builtins.open', new_callable=mock_open)
    def test_load_students_invalid_json(self, mock_file) -> None:
        """Return an empty list and log an exception for invalid JSON."""
        
        mock_file.return_value.read.return_value = 'invalid_json_format'
        
        result = self.storage.load_students()
        
        self.assertEqual(result, [])
        self.mock_logger.exception.assert_called_once()
    
    @patch('builtins.open', side_effect=Exception('Unexpected error'))
    def test_load_students_unexpected_exception(self, mock_file) -> None:
        """Return an empty list and log an exception for unexpected failures."""
        
        result = self.storage.load_students()
        
        self.assertEqual(result, [])
        self.mock_logger.exception.assert_called_once()
        
    @patch('builtins.open', new_callable=mock_open)
    def test_save_students_success(self, mock_file) -> None:
        """Persist students as correctly formatted JSON and return True."""
        
        result = self.storage.save_students(self.sample_students)
        
        self.assertTrue(result)
        mock_file.assert_called_once_with(self.file_name, 'w', encoding='utf-8')
        
        handle = mock_file.return_value
        written_content = "".join(call.args[0] for call in handle.write.call_args_list)
        
        expected_json = json.dumps(self.sample_students, indent=4, ensure_ascii=False)
        
        self.assertEqual(json.loads(written_content), self.sample_students)
        self.assertEqual(written_content, expected_json)
        
        
    @patch('builtins.open', side_effect=IOError('Memory Full'))
    def test_save_students_ioerror(self, mock_file) -> None:
        """Return False and log an exception when writing fails with IOError."""
        
        result = self.storage.save_students(self.sample_students)
        
        self.assertFalse(result)
        self.mock_logger.exception.assert_called_once()
        
    @patch('builtins.open', side_effect=Exception("Unauthorized error!"))
    def test_save_students_unexpected_exception(self, mock_file) -> None:
            """Return False and log an exception for unexpected write failures."""
        
        result = self.storage.save_students(self.sample_students)
        
        self.assertFalse(result)
        self.mock_logger.exception.assert_called_once()
        
if __name__ == "__main__":
    unittest.main()