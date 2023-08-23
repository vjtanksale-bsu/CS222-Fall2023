def main():
    students = ["Mark", "Jane", "John", "Mary"]
    classes = ["CS120", "CS121", "CS222"]
    i = 0
    while i < len(students):
        j = 0
        while j < len(classes):
            if students[i][0] == "M":
                print(students[i] + " received an A in " + classes[j])
            j += 1
        i += 1


main()
