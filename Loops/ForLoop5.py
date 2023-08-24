def main():
    for i in range(0, 4):
        print(f"Outer loop {i}")
        for j in range(0, 3):
            print(f"Inner loop {j}")
    for counter in range(10):
        if (counter % 2 == 0):
            print(f"Counter: {counter}")
    afcSouth = ["Colts", "Titans", "Texans", "Jaguars"]
    print(len(afcSouth))
    print(len(afcSouth[0]))
    print(afcSouth[3][2])
    exams = [[75, 82, 93], [100, 92, 97], [50, 90, 80]]
    for exam in exams:
        for score in exam:
            if not score >= 60:
                print(score)

main()