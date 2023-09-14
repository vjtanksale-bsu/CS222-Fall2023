import math
def IsPrime(n):
    for counter in range(2, int(math.sqrt(n)) + 1):
        if n % counter == 0:
            return False
    return True