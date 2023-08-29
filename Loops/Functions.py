def FahToCel(fah):
    return (fah - 32) * 5.0 / 9.0
def PrintMenu():
    print("Bunch of print statements")
def Year(credits = 0):
    if credits >= 90:
        return "Senior"
    elif credits >= 60:
        return "Junior"
    elif credits >= 30:
        return "Sophomore"
    else:
        return "Freshman"

def DefaultValues(x = 0, y = 0, z = 0):
    print(x)
    print(y)
    print(z)

DefaultValues(5, 2)
#print(Year(100))
#PrintMenu()
#print(FahToCel(50))
