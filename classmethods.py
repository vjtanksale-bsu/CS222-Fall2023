class Student:
    numberOfStudents = 0
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName 
    def printStudent(self):
        print(self.lastName + ", " + self.firstName)
    
    @classmethod
    def updateStudents(cls):
        cls.numberOfStudents += 1

alice = Student("Alice", "Jones")
Student.updateStudents()
bob = Student("Bob", "Smith")
Student.updateStudents()
print(alice.numberOfStudents)
print(bob.numberOfStudents)


