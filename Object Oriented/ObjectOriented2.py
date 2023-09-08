class Student:
    def __init__(self, name, roll):
        self.__name = name
        self.roll = roll

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


student = Student("Alice", 101)
print(student.get_name())
student.set_name("Bob")
print(student.get_name())
