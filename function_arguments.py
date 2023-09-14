def SayHello(firstName, lastName):
    print("Hello " + firstName + " " + lastName)
#SayHello('John', 'Doe')
#SayHello(lastName='Doe', firstName='John')

def Sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(result)
#Sum(2, 3)
#Sum(2, 3, 10)

Greeting = lambda : print('Hello World')
Greeting()

GreetingName = lambda name : print('Hello ', name)
GreetingName('John Doe')

def Statistics(midterm : list) -> list:
    return sum(midterm), max(midterm), min(midterm), sum(midterm)/float(len(midterm))

print(Statistics([90, 82, 100, 72, 91, 57]))