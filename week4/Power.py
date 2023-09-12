from ast import Pow
from contextlib import nullcontext
from lib2to3.pgen2.token import NUMBER


class Power(object):

 
    default_exponent = 2
 
    def __init__(self, exponent=default_exponent):
        self.exponent = exponent
 
    def of(self, x):
        return x ** self.exponent
 
class RealPower(Power):  
 
    def of(self, x):
        if isinstance(self.exponent, int) or x >= 0:
            return x ** self.exponent
        raise ValueError(
            'Fractional powers of negative numbers are imaginary')

def main():
    number0 = Power(5)
    print(number0.of(3))
    number1 = RealPower(1/3)
    print(number1.of(-3.5))

main()