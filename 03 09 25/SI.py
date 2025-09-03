#SimpleInterest
p=int(input("Principle amount: "))
t=int(input("No.of months: "))
r=int(input("Rate of interest: "))
SI=(p*t*r)/100
TA=SI+p
print("Simple Interest: ",SI)
print("Total Amount: ",TA)