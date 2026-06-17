class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  def area(self):
    s = self.width * self.height
    
    print(f"\nIf the width is {self.width} and the area height is {self.height}, the area is {s}")
    print(f"because {self.width} times {self.height} is 50")
    
  def perimeter(self):
    p = 2 * (self.width + self.height)
    
    print(f"\nThe perimeter is {p} because {self.width} plus {self.height} multiplied by 2 is {p}")
    
rectangle = Rectangle(5, 10)
rectangle.area()
rectangle.perimeter()