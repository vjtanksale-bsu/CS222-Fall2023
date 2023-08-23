def main():
    students = ["Mark", "Jane", "John", "Mary"]
    classes = ["CS120", "CS121", "CS222"]
    for student in students:
        for clas in classes:
            print(f"{student} is taking class {clas}")
        print("--------------------------")

main()