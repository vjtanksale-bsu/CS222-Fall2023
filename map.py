def square(x):
    return x**2
numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)
squaresList = list(squares)
print(squaresList)

fruits = ["apple", "banana", "cherry"]
wordLengths = list(map(len, fruits))
print(wordLengths)
def ConvertToUpper(n):
    return n.upper()

names = ["alice", "bob", "carol", "dave", "eve"]
uppercaseNames = list(map(ConvertToUpper, names))
print(uppercaseNames)

def FahToCel(fah):
    return (fah - 32) * 5.0 / 9.0
fahrenheitTemperatures = [212, 32, 100]
celsiusTemperatures = list(map(FahToCel, fahrenheitTemperatures))
print(celsiusTemperatures)
