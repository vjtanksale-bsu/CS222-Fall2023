def main():
    students = ["Mark", "Jane", "John", "Mary"]
    classes = ["CS120", "CS121", "CS222"]
    for student in students:
        for clas in classes:
            if student[0] == "M":
                print(student + " received an A in " + clas)


main()
