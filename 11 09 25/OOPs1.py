class Student:
    def __init__(self,name,rno,marks):
        self.name=name
        self.rno=rno
        self.marks=marks
        
    def Details(self):
        print("Student details")
        print(self.name)
        print(self.rno)
        print(self.marks)
    

s1=Student("Amaira",580,96)
s1.Details()
s2=Student("Anvika",348,65)
s2.Details()