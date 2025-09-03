#Student details
Sno=int(input("RollNumber: "))
Sname=input("Name: ")
s1=int(input("Subject1 marks: "))
s2=int(input("Subject2 marks: "))
s3=int(input("Subject3 marks: "))
Total=s1+s2+s3
Avg=Total/3
print("Name: ",Sname)
print("RollNumber: ",Sno)
print("Total score: ",Total)
print("Average score: ",round(Avg,2))