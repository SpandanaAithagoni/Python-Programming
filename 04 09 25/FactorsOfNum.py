#Print all the factors of a number
def Factors(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i,end=" ")
            
q=int(input("Enter a number: "))
Factors(q)