"""
Unit tests for the `MovieStorage` persistence layer.

This test suite verifies the behavior of `storage.MovieStorage` in
complete isolation from the real filesystem and logging subsystem.
All disk I/O is intercepted via `unittest.mock.patch` on `builtins.open`
(and, where appropriate, `mock_open`), and the module-level logger
factory (`storage.get_logger`) is patched so that no test writes to
stdout or to an actual log file.

The suite exercises every control-flow branch in `MovieStorage`:

    * `get_default_movies` — static seed-data generation.
    * `load_movies` — successful load, missing file (with both a
      successful and a failed fallback save), corrupted JSON, and an
      unexpected exception during read.
    * `save_movies` — successful write, `IOError` during write, and
      an unexpected exception during write.

Together these tests provide 100% line and branch coverage of
`storage.py`.
"""

import unittest
import json
from unittest.mock import patch, mock_open
from storage import MovieStorage

class TestMovieStorage(unittest.TestCase):
    """
    Test suite for the `MovieStorage` class.

    Each test targets a single method or a single execution branch of
    `MovieStorage`, ensuring that success paths return the expected
    data and that failure paths (missing file, malformed JSON, I/O
    errors, unexpected exceptions) are handled gracefully and logged
    rather than propagated to the caller.

    Filesystem access is never performed for real: `builtins.open` is
    patched in every test that touches `load_movies` or `save_movies`,
    and the application logger is replaced with a mock so that
    logging calls can be asserted without side effects.
    """
    
    def setUp(self):
        """
        Prepare a fresh `MovieStorage` instance and test fixtures.

        Patches `storage.get_logger` so that `MovieStorage` receives a
        mock logger instead of a real one, then instantiates
        `MovieStorage` with a dummy file name. Also prepares a small
        sample movie dictionary and its JSON-serialized form, reused
        across multiple test cases.
        """
        
        # Safely patch the logger to verify logging behavior without writing to stdout/files
        self.logger_patcher = patch('storage.get_logger')
        self.mock_get_logger = self.logger_patcher.start()
        self.mock_logger = self.mock_get_logger.return_value
        
        # Initialize test fixtures (dummy file name and sample data)
        self.file_name = 'test_movies.json'
        self.storage = MovieStorage(self.file_name)
        self.sample_movies = {
            "action": ["Inception", "The Matrix"],
            "sci-fi": ["Interstellar"]
        }
        self.sample_json_str = json.dumps(self.sample_movies)
        
    def tearDown(self):
        """Stop the logger patcher to restore the original `get_logger`."""
        
        self.logger_patcher.stop()
        
    def test_get_default_movies(self):
        """
        `get_default_movies` should return a well-formed seed dataset.

        Verifies that the static method returns a dictionary, that it
        contains the expected genre keys, that a known sample title
        is present under the "action" genre, and that the genre lists
        are non-empty.
        """
        
        default_movies = MovieStorage.get_default_movies()
        
        self.assertIsInstance(default_movies, dict)
        self.assertIn("action", default_movies)
        self.assertIn("sci-fi", default_movies)
        self.assertIn("John Wick", default_movies['action'])
        self.assertTrue(len(default_movies['action']) > 0)
    
    def test_load_movies_success(self):
        """
        `load_movies` should return the parsed contents of an existing file.

        Simulates a JSON file already present on disk by mocking
        `builtins.open` with `mock_open(read_data=...)`. Verifies that
        the returned dictionary matches the sample data and that the
        file was opened in read mode with UTF-8 encoding.
        """
        
        m = mock_open(read_data=self.sample_json_str)
        with patch('builtins.open', m):
    
            result = self.storage.load_movies()
        
        self.assertEqual(result, self.sample_movies)
        m.assert_called_once_with(self.file_name, 'r', encoding='utf-8')
    
    @patch('builtins.open', side_effect=FileNotFoundError) 
    @patch.object(MovieStorage, 'save_movies')
    def test_load_movies_file_not_found_save_success(self, mock_save, mock_file):
        """
        `load_movies` should bootstrap and persist defaults when the file is missing.

        Simulates a missing storage file by making `open` raise
        `FileNotFoundError`. Verifies that `load_movies` falls back to
        `get_default_movies`, attempts to persist that default dataset
        via `save_movies`, returns the defaults when the save
        succeeds, and logs the missing-file condition at debug level.

        Args:
            mock_save (MagicMock): Patched `MovieStorage.save_movies`,
                configured to return `True` to simulate a successful save.
            mock_file (MagicMock): Patched `builtins.open`, configured
                to raise `FileNotFoundError` on every call.
        """
        
        mock_save.return_value = True
        
        result = self.storage.load_movies()
        expected_defaults = self.storage.get_default_movies()
        
        self.assertEqual(result, expected_defaults)
        self.mock_logger.debug.assert_called_once()
        mock_save.assert_called_once_with(expected_defaults)
        
    @patch('builtins.open', side_effect=FileNotFoundError)
    @patch.object(MovieStorage, 'save_movies')
    def test_load_movies_file_not_found_save_failure(self, mock_save, mock_file):
        """
        `load_movies` should return an empty dict when the fallback save fails.

        Simulates a missing storage file, as above, but configures the
        subsequent `save_movies` call to fail. Verifies that
        `load_movies` does not propagate the failure or raise an
        exception, but instead returns an empty dictionary while still
        logging the missing-file condition and attempting the save
        exactly once with the default dataset.

        Args:
            mock_save (MagicMock): Patched `MovieStorage.save_movies`,
                configured to return `False` to simulate a failed save.
            mock_file (MagicMock): Patched `builtins.open`, configured
                to raise `FileNotFoundError` on every call.
        """
        
        mock_save.return_value = False
        
        result = self.storage.load_movies()
        
        self.assertEqual(result, {})
        self.mock_logger.debug.assert_called_once()
        mock_save.assert_called_once_with(self.storage.get_default_movies())
        
    def test_load_movies_invalid_json(self):
        """
        `load_movies` should return an empty dict when the file contains malformed JSON.

        Simulates a corrupted storage file by mocking `builtins.open`
        to return non-JSON content. Verifies that `load_movies` catches
        the resulting `json.JSONDecodeError`, returns an empty
        dictionary instead of raising, and logs the failure via
        `logger.exception`.
        """
        
        m = mock_open(read_data='invalid_json_format')
        with patch('builtins.open', m):
        
            result = self.storage.load_movies()
        
        self.assertEqual(result, {})
        self.mock_logger.exception.assert_called_once()
        
    @patch('builtins.open', side_effect=Exception('Unexpected load error'))
    def test_load_movies_unexpected_exception(self, mock_file):
        """
        `load_movies` should return an empty dict on any unexpected error.

        Simulates an unforeseen failure (e.g. a permissions error or
        hardware fault) by making `open` raise a generic `Exception`.
        Verifies that `load_movies` catches the error via its
        catch-all handler, returns an empty dictionary, and logs the
        failure via `logger.exception`.

        Args:
            mock_file (MagicMock): Patched `builtins.open`, configured
                to raise a generic `Exception` on every call.
        """
        
        result = self.storage.load_movies()
        
        self.assertEqual(result, {})
        self.mock_logger.exception.assert_called_once()
    
    @patch('builtins.open', new_callable=mock_open)    
    def test_save_movies_success(self, mock_file):
        """
        `save_movies` should write the dictionary to disk as pretty-printed JSON.

        Verifies that the method returns `True` on success, that the
        file is opened in write mode with UTF-8 encoding, and that the
        exact JSON content written to the file handle matches
        `json.dumps` output with 4-space indentation and
        `ensure_ascii=False`, by reassembling all chunks passed to the
        mocked handle's `write` calls.

        Args:
            mock_file (MagicMock): Patched `builtins.open`, used to
                intercept and inspect all writes to the storage file.
        """
        
        result = self.storage.save_movies(self.sample_movies)
        
        self.assertTrue(result)
        mock_file.assert_called_once_with(self.file_name, 'w', encoding='utf-8')
        
        handle = mock_file()
        written_content = "".join(call.args[0] for call in handle.write.call_args_list)
        expected_json = json.dumps(self.sample_movies, indent=4, ensure_ascii=False)
        
        self.assertEqual(written_content, expected_json)
        
    @patch('builtins.open', side_effect=IOError('Memory Full'))
    def test_save_movies_io_error(self, mock_file):
        """
        `save_movies` should return False and log when an IOError occurs.

        Simulates a disk-level failure (e.g. insufficient storage
        space) by making `open` raise `IOError`. Verifies that
        `save_movies` catches the error, returns `False` instead of
        raising, and logs the failure via `logger.exception`.

        Args:
            mock_file (MagicMock): Patched `builtins.open`, configured
                to raise `IOError` on every call.
        """
        
        result = self.storage.save_movies(self.sample_movies)
        
        self.assertFalse(result)
        self.mock_logger.exception.assert_called_once()
        
    @patch('builtins.open', side_effect=Exception('Unauthorized error!'))
    def test_save_movies_unexpected_exception(self, mock_file):
        """
        `save_movies` should return False and log on any unexpected error.

        Simulates an unforeseen failure (e.g. a permissions error)
        during write by making `open` raise a generic `Exception`.
        Verifies that `save_movies` catches the error via its
        catch-all handler, returns `False`, and logs the failure via
        `logger.exception`.

        Args:
            mock_file (MagicMock): Patched `builtins.open`, configured
                to raise a generic `Exception` on every call.
        """
        
        result = self.storage.save_movies(self.sample_movies)
        
        self.assertFalse(result)
        self.mock_logger.exception.assert_called_once()
        
        
if __name__ == "__main__":
    unittest.main()