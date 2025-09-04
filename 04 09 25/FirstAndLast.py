#Print first and last digits of a number
def FandL(n):
    last=n%10
    rem=0
    while(n>0):
        rem=n%10
        n=n//10
    return last,rem

w=int(input("Enter a number: "))
print(FandL(w))
    