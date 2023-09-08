class Parent1:
    def speak(self):
        return "Parent 1 says hello"


class Parent2:
    def greet(self):
        return "Parent 2 greets you"


class Child(Parent1, Parent2):
    pass


child = Child()
print(child.speak())
print(child.greet())
