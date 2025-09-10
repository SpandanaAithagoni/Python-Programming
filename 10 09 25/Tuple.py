def highMark(Student):
    max=0
    name=0
    for i in range(len(Student)):
        if Student[i][2]>max:
            max=Student[i][2]
            name=i
    print("Highest Score: ",Student[name][1])

def Score75(Student):
    score=75
    for i in range(len(Student)):
        if Student[i][2]>score:
            print(Student[i][1])
            

Student=[(584,"Mahira",95),(590,"Kaira",60),(594,"Amaira",72),(599,"Naksh",90)]  
highMark(Student)
Score75(Student)