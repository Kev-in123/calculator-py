class Calc:
    def __init__(self, num1, num2) -> float:
      self.num1 = num1
      self.num2 = num2
    
    def add(self):
      return self.num1 + self.num2

    def divide(self):
      return self.num1 / self.num2

    def multiply(self):
      return self.num1 * self.num2

    def subtract(self):
      return self.num1 - self.num2

    def pow(self):
      return self.num1 ** self.num2

    def sqrt(self):
      return self.num1 ** 0.5
