#Sum of n natural numbers
def SumOfN(n):
    i=1
    sum=0
    while(i<=n):
        sum=sum+i
        i=i+1
    return sum

w=int(input("Enter n:"))
print(SumOfN(w))