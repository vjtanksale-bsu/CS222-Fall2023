def main():
    students = {}
    fileHandle = open("students.txt", "r")
    fileData = fileHandle.readlines()
    for lines in fileData:
        parts = lines.split(',')
        students[parts[0]] = [parts[1], parts[2], parts[3], parts[4]]
    fileHandle.close()
    print(students)
main()