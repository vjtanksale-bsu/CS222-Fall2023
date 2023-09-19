def SumofOdd(a, b):
    result = 0
    for x in range(a, b + 1):
        if x % 2 == 1:
            result += x
    return result

def Tuition(n):
    result = 8000.00
    percent = 1.03
    for x in range(n):
        result *= percent
    return round(result, 2)