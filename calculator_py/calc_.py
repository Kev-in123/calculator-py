import math
from .errors import InvalidArgument

class Calc:
    def __init__(self, num1, num2) -> float:
      self.num1 = num1
      self.num2 = num2
      
    def add(self):
      return self.num1 + self.num2

    def divide(self):
      if self.num2 == 0:
        raise InvalidArgument("Division by 0")
      return self.num1 / self.num2

    def multiply(self):
      return self.num1 * self.num2

    def subtract(self):
      return self.num1 - self.num2

    def pow(self):
      return self.num1 ** self.num2

    def sqrt(self):
      if self.num1 < 0:
        raise InvalidArgument("Domain error")
      return self.num1 ** 0.5

    def log(self):
      if self.num1 < 0 or self.num2 < 0:
        raise InvalidArgument("Domain error")
      return math.log(self.num1, self.num2)

    def gcd(self):
      return math.gcd(self.num1, self.num2)

    def lcm(self):
      return self.multiply()//self.gcd()
    
    def factorial(self):
      if self.num1 < 0:
        raise InvalidArgument("Domain error")
      return math.factorial(self.num1)

    def sin(self):
      return math.sin(self.num1)
    
    def cos(self):
      return math.cos(self.num1)

    def tan(self):
      return math.tan(self.num1)
    
    def asin(self):
      if -1 > self.num1 > 1:
        raise InvalidArgument("Domain error")
      return math.asin(self.num1)
    
    def acos(self):
      if -1 > self.num1 > 1:
        raise InvalidArgument("Domain error")
      return math.acos(self.num1)
    
    def atan(self):
      if -1 > self.num1 > 1:
        raise InvalidArgument("Domain error")
      return math.atan(self.num1)
