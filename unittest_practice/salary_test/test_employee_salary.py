import unittest
from employee_salary import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.employee = Employee(1000)
        
    def test_give_defualt_raise(self):
        result = self.employee.give_raise()
        self.assertEqual(result, 6000)
        
    def test_give_custom_raise(self):
        result = self.employee.give_raise(2000)
        self.assertEqual(result, 3000)
        
if __name__ == "__main__":
    unittest.main()