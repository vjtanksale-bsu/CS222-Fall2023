def main():
    students = ["Mark", "Jane", "John", "Mary"]
    classes = ["CS120", "CS121", "CS222"]
    for student in students:
        for c in classes:
            print(f"{student} is taking class {c}")
        print("--------------------------")

main()
