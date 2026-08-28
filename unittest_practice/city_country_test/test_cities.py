import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    
    def test_city_country(self):
        
        result = city_country('  kohnaurganch ', '  turkmaniston ', ' 6700')
        self.assertEqual(result, 'Kohnaurganch, Turkmaniston - Population 6700')
        
if __name__ == "__main__":
    unittest.main()