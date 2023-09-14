class Calculator():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def GetSum(self):
        return self.x + self.y
    def GetDifference(self):
        return self.x - self.y
    def GetQuotient(self):
        return self.x / self.y