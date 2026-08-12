import unittest
from unittest.mock import patch, mock_open
from greeting_logger import log_greeting

class TestLogGreeting(unittest.TestCase):
    
    @patch('builtins.open', new_callable=mock_open)
    def test_log_greeting_success(self, mock_file):
        
        result = log_greeting('Behruz')
        self.assertTrue(result)
        
        handle = mock_file()
        written_content = "".join(call.args[0] for call in handle.write.call_args_list)
        self.assertEqual("Hello, Behruz!\n", written_content)
        
        
    @patch('builtins.open', new_callable=mock_open)
    def test_log_greeting_opens_correct_mode(self, mock_file):
        
        result = log_greeting('Behruz')
        
        mock_file.assert_called_once_with('greetings.txt', 'a', encoding='utf-8')
        
if __name__ == "__main__":
    unittest.main()