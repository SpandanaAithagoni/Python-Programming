#Factorial of a number
def Fact(n):
    i=1
    fact=1
    while(i<=n):
        fact=fact*i
        i=i+1
    return fact

w=int(input("Enter a number: "))
print(Fact(5))