#Sum of the digits of a number
def SumOfD(n):
    sum=0
    rem=0
    while(n>0):
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
w=int(input("Enter a number: "))
print(SumOfD(w))