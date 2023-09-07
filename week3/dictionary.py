def main():
    #finalExamScores = [100, 82, 93, 81, 55, 72]
    finalExamScores = {
        "Alice" : 100,
        "Bob" : 82,
        "Carol" : 93,
        "Dave" : 81,
        "Eve" : 55,
        "Frank" : 72
    }
    print("Gary" in finalExamScores.keys())
    print(finalExamScores.get('Carol'))
    print(finalExamScores.get('Harry'))
    #print(finalExamScores["Eve"])
    finalExamScores["Eve"] = 57
    #print(finalExamScores["Eve"])

    #for key, value in finalExamScores.items():
    #    print(value)
    #for v in finalExamScores.values():
    #    print(v)
    #for k in finalExamScores.keys():
    #    print(k)
    students = [
        {
            "firstName" : "Alice",
            "lastName" : "Smith",
            "major": "Chemistry",
            "gpa" : 3.92,
            "courses" : ["MATH 165", "CS 222", "CS 230"]
        },
        {
            "firstName" : "Bob",
            "lastName" : "Jones",
            "major": "Physics",
            "gpa" : 3.3,
            "courses" : ["CS 222", "MATH 166"]
        }
    ]
    print(len(students))
    for s in students:
        #if s["major"] == "Physics":
        #    print(s["lastName"] + ", " + s["firstName"])
        #if s["gpa"] > 3.5:
        #    print(s)
        if "MATH 165" in s["courses"]:
            print(s["lastName"] + ", " + s["firstName"])
    #print(alice["courses"][2])
    #for c in bob["courses"]:
    #    print(c)
    
main()