def main():
    students = ["Mark", "Jane", "John", "Mary"]
    classes = ["CS120", "CS121", "CS222"]
    i = 0
    while i < len(students):
        j = 0
        while j < len(classes):
            print(f"{students[i]} is taking class {classes[j]}")
            j += 1
        print("--------------------------")
        i += 1

main()
