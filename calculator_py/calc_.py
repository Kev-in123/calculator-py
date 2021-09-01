import math
from .errors import CalcError

class Calc:
    def __init__(self, num1, num2) -> float:
      self.num1 = num1
      self.num2 = num2
         
    def __getattr__(self, attr):
        raise AttributeError(attr)

    def add(self):
        return self.num1 + self.num2

    def divide(self):
        if self.num2 == 0:
          raise CalcError("Division by 0")
        else:
          return round(self.num1 / self.num2, 5)

    def multiply(self):
        return self.num1 * self.num2

    def subtract(self):
        return self.num1 - self.num2

    def pow(self):
        return self.num1 ** self.num2

    def sqrt(self):
        if self.num1 < 0:
          raise CalcError("Domain error")
        else:
          return round(self.num1 ** 0.5, 5)

    def log(self):
        if self.num1 < 0 or self.num2 < 0:
          raise CalcError("Domain error")
        else:
          return round(math.log(self.num1, self.num2), 5)

    def gcd(self):
        return math.gcd(self.num1, self.num2)

    def lcm(self):
        return self.num1 * self.num2//math.gcd(self.num1, self.num2)
    
    def factorial(self):
        if self.num1 < 0:
          raise CalcError("Domain error")
        else:
          return math.factorial(self.num1)

    def sin(self):
        return round(math.sin(self.num1), 5)
    
    def cos(self):
        return round(math.cos(self.num1), 5)

    def tan(self):
        return round(math.tan(self.num1), 5)
    
    def asin(self):
        if self.num1 not in range(-1, 2):
          raise CalcError("Domain error")
        else:
          return round(math.asin(self.num1), 5)
    
    def acos(self):
        if self.num1 not in range(-1, 2):
          raise CalcError("Domain error")
        else:
          return round(math.acos(self.num1), 5)
    
    def atan(self):
        if self.num1 not in range(-1, 2):
          raise CalcError("Domain error")
        else:
          return round(math.atan(self.num1), 5)


    def get_area(num_of_sides, len_of_side):
      apothem = len_of_side/(2 * math.tan(math.radians(180/num_of_sides)))
      area = num_of_sides * len_of_side * apothem/2
      return round(area, 5)