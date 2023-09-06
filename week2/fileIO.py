def main():
    try:
        studentList = open("students.txt", 'r')
        students = studentList.readlines()
        studentList.close()
        #print(students)
        for s in students:
            #print(s)
            parts = s.split(',')
            #print(parts[2])
            if parts[0] == "Smith":
                print(s)
    except FileNotFoundError:
        print("File not found")
main()