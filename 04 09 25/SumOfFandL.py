#Print sum of first and last digits of a number
def FandL(n):
    last=n%10
    rem=0
    sum=0
    while(n>0):
        rem=n%10
        n=n//10
    sum=last+rem
    return sum
w=int(input("Enter a number: "))
print(FandL(w))
    