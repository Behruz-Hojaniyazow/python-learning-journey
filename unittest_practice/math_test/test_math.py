import unittest
from math_add import add

class TestMathAdd(unittest.TestCase):
    
    def test_add_positive_integers(self):
        
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(100, 300), 400)
        
    def test_add_negative_integers(self):
        
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-5, 5), 0)
        
    def test_add_floats(self):
        
        self.assertAlmostEqual(add(0.1, 0.3), 0.4, places=7)
        self.assertAlmostEqual(add(0.5, 0.3), 0.8, places=7)
        
    def test_add_strings(self):
        
        self.assertEqual(add("Hello, ", "Behruz"), "Hello, Behruz")
        
    def test_add_lists(self):
        
        self.assertEqual(add([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(add(['2', 5.4, 'seven', -8], [-8.3, '-4.5']), ['2', 5.4, 'seven', -8, -8.3, '-4.5'])
        
    def test_add_zeros(self):
        
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, -5), -5)
        
    def test_add_type_error_int_str(self):
        with self.assertRaises(TypeError):
            add(5, '5')
            
    def test_add_type_error_str_int(self):
        with self.assertRaises(TypeError):
            add('5', 5)
            
if __name__ == "__main__":
    unittest.main()