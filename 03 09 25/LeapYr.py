#Leap Year
def leapYr(n):
    if((n%4==0 and n%100!=0) or (n%100==0 and n%400==0)):
        print("It is a leap year")
    else:
        print("It is not a leap year")

k=int(input("Enter the year: "))
leapYr(k)