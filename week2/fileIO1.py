def main():
    fileData = open("students.txt", "r")
    students = fileData.readlines()
    fileData.close()
    fileOutput = open("output.txt", "a")
    for s in students:
        parts = s.split(',')
        #print(parts)
        gpa = float(parts[3])
        fileOutput.write(parts[1] + "'s GPA is " + str(gpa) + "\n")
    fileOutput.close()
main()