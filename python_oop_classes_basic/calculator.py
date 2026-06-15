class Calculator:
  def __init__(self, number1, number2):
    self.number1 = number1
    self.number2 = number2
    
  def add(self):
    result = self.number1 + self.number2
    print(f"{self.number1} + {self.number2} = {result}")
    
  def subtract(self):
    result = self.number1 - self.number2
    print(f"{self.number1} - {self.number2} = {result}")
    
  def multiply(self):
    result = self.number1 × self.number2
    print(f"{self.number1} * {self.number2} = {result}")
    
  def divide(self):
    result = self.number1 / self.number2
    clean_result = int(result) if result.is_integer() else result
    print(f"{self.number1} ÷ {self.number2} = {clean_result}")
    
numbers = Calculator(10, 5)
numbers.add()
numbers.subtract()
numbers.multiply()
numbers.divide()