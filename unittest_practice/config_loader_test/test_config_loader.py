import unittest
from unittest.mock import patch, mock_open
from config_loader import ConfigLoader

class TestConfigLoader(unittest.TestCase):
    
    def setUp(self):
        self.file_name = "test_logger.txt"
        self.config_loader = ConfigLoader(self.file_name)
        
    def test_validate_with_required_keys(self):
        
        config = {'host': 'x', 'port': '8090'}
        
        result = self.config_loader.validate(config)
        self.assertTrue(result)
        
    def test_validate_missing_keys(self):
        
        config = {'name': 'behruz', 'b_year': '2008'}
        
        result = self.config_loader.validate(config)
        self.assertFalse(result)
    
    @patch('builtins.open', new_callable=mock_open, read_data="host=localhost\nport=8080\n")
    def test_load_config_success(self, mock_file):
        
        result = self.config_loader.load_config()
        self.assertEqual(result, {"host": "localhost", "port": "8080"})
        
        
    
    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_load_config_file_not_found(self, mock_file):
        
        result = self.config_loader.load_config()
        
        self.assertEqual(result, {})
        
    @patch('builtins.open', new_callable=mock_open)
    @patch.object(ConfigLoader, 'validate')
    def test_load_config_invalid_data(self, mock_validate, mock_file):
        
        mock_validate.return_value = False
        
        result = self.config_loader.load_config()
        self.assertEqual(result, {})
        
if __name__ == "__main__":
    unittest.main()