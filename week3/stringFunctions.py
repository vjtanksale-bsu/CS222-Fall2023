def main():
    finalExamScores = [100, 82, 93, 81, 55, 72]
    print(finalExamScores[2:])
    print(finalExamScores[:3])
    finalExamScores[3] = 10
    print(finalExamScores[1:4])

    bsu = "Ball State University"
    bsu[2] = 'x'
    print(bsu[:12])
    print(bsu[-5:-3])
    print(bsu[-3:-5])
    #for letter in bsu:
    #    print(letter)
main()