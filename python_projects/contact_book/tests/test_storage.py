"""
Unit test suite for the persistent storage module of the Contact Book application.

This module contains comprehensive test cases for the `JSONContactStorage` class.
It utilizes the `unittest` framework and `unittest.mock` library to fully isolate 
file system operations (I/O) and logging mechanisms from the core business logic.
The tests ensure robust data serialization, deserialization, and rigorous edge-case 
handling without creating or modifying actual files on the disk.
"""

import unittest
import json
from storage import JSONContactStorage
from unittest.mock import patch, mock_open

class TestJSONContactStorage(unittest.TestCase):
    """
    Test cases for the JSONContactStorage class.

    This suite validates both the "happy paths" (successful read/write) and 
    the "unhappy paths" (missing files, corrupted JSON, system I/O errors) 
    to guarantee the storage layer's reliability and resilience.
    """
    
    def setUp(self):
        """
        Configure the test environment and initial state before each test execution.

        This method patches the external logger to prevent actual log emission 
        during testing and initializes the storage instance with a dummy file name.
        It also sets up standard mocked contact data used across multiple test cases.
        """
        
        # Safely patch the logger to verify logging behavior without writing to stdout/files
        self.logger_patcher = patch("storage.get_logger")
        self.mock_get_logger = self.logger_patcher.start()
        self.mock_logger = self.mock_get_logger.return_value
        
        # Initialize test fixtures (dummy file name and sample data)
        self.file_name = "test_contacts.json"
        self.storage = JSONContactStorage(self.file_name)
        self.sample_contacts = [{"name": "Behruz", "phone": "+99363807476"}]
        self.sample_json_str = json.dumps(self.sample_contacts)
        
    def tearDown(self):
        """
        Clean up the test environment after each test execution.

        Stops the logger patcher to prevent side effects or mock leakage 
        into other test suites running in the same process.
        """
        
        self.logger_patcher.stop()
        
    @patch('builtins.open', new_callable=mock_open)
    def test_load_contacts_success(self, mock_file):
        """
        Test successful loading of contact data from a valid JSON file.

        Simulates opening an existing file containing valid JSON data.
        Asserts that the file is opened with the correct mode and encoding,
        and verifies that the returned list strictly matches the mock data.
        """
        
        mock_file.return_value.read.return_value = self.sample_json_str
        
        result = self.storage.load_contacts()
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], "Behruz")
        
        mock_file.assert_called_once_with(self.file_name, 'r', encoding='utf-8')
        
    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_load_contacts_file_not_found(self, mock_file):
        """
        Test behavior when the storage file does not exist.

        Simulates a `FileNotFoundError` (e.g., first-time application launch).
        Asserts that the method safely handles the exception, returns an empty list,
        and triggers a `debug` level log message rather than crashing.
        """
        
        result = self.storage.load_contacts()
        
        self.assertEqual(result, [])
        
        self.mock_logger.debug.assert_called_once()
        
    @patch('builtins.open', new_callable=mock_open)
    def test_load_contacts_invalid_json(self, mock_file):
        """
        Test behavior when the storage file contains malformed JSON data.

        Simulates reading a corrupted or invalid JSON string from the file.
        Asserts that the application intercepts the decoding error, returns 
        an empty list as a fallback, and logs the exception correctly.
        """
        
        mock_file.return_value.read.return_value = 'invalid_json_format'
        
        result = self.storage.load_contacts()
        
        self.assertEqual(result, [])
        
        self.mock_logger.exception.assert_called_once()
        
    
    @patch('builtins.open', side_effect=Exception('Unexpected error'))
    def test_load_contacts_unexpected_exception(self, mock_file):
        """
        Test fallback behavior against unforeseen errors during data loading.

        Simulates an unpredictable runtime exception during the file read operation.
        Asserts that the broad exception block captures the error, prevents a crash,
        returns an empty list, and records a critical exception log.
        """
        
        result = self.storage.load_contacts()
        
        self.assertEqual(result, [])
        self.mock_logger.exception.assert_called_once()
        
    @patch('builtins.open', new_callable=mock_open)
    def test_save_contacts_success(self, mock_file):
        """
        Test successful serialization and saving of contact data.

        Validates that the given contact list is properly converted into an indented
        JSON string with non-ASCII characters preserved. It captures all chunked write
        calls made by `json.dump` to strictly verify the final output structure.
        """
        
        result = self.storage.save_contacts(self.sample_contacts)
        
        self.assertTrue(result)
        mock_file.assert_called_once_with(self.file_name, 'w', encoding='utf-8')
        
        handle = mock_file()
        written_content = "".join(call.args[0] for call in handle.write.call_args_list)
        expected_json = json.dumps(self.sample_contacts, indent=4, ensure_ascii=False)
        
        self.assertEqual(written_content, expected_json)
        
    @patch('builtins.open', side_effect=IOError('Memory Full'))
    def test_save_contacts_io_error(self, mock_file):
        """
        Test failure handling when system I/O errors occur during saving.

        Simulates an environment restriction (e.g., disk full, permission denied).
        Asserts that the method returns `False` indicating failure and logs 
        the specific I/O exception accurately.
        """
        
        result = self.storage.save_contacts(self.sample_contacts)
        
        self.assertFalse(result)
        
        self.mock_logger.exception.assert_called_once()
    
    @patch('builtins.open', side_effect=Exception("Unauthorized error!"))    
    def test_save_contacts_unexpected_exception(self, mock_file):
        """
        Test fallback behavior against unforeseen errors during data saving.

        Simulates a random runtime exception while attempting to write to the file.
        Asserts that the error is gracefully caught, `False` is returned, 
        and the system state remains stable while logging the event.
        """
    
        result = self.storage.save_contacts(self.sample_contacts)
        
        self.assertFalse(result)
        self.mock_logger.exception.assert_called_once()
        
if __name__ == '__main__':
    unittest.main()