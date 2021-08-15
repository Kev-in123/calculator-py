class CalcError(Exception):
    def __init__(self, error):
      self.message = error
      super().__init__(self.message)
