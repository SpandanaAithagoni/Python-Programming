#Student Grades
def StuRes(n):
    if(n>80):
        print("Distinction")
    elif(n>70 and n<=80):
        print("A")
    elif(n>50 and n<=70):
        print("B")
    elif(n>=40 and n<=50):
        print("C")
    else:
        print("Fail")
k=int(input("Enter the marks for the grades: "))
StuRes(k)
