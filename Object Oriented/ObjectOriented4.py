class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks")


dog1 = Dog("Ava", "German Shepard")
dog2 = Dog("Roofus", "Doberman")

# Accessing object properties and calling methods
print(f"{dog1.name} is a {dog1.breed}")
dog2.bark()
