#Check whether a number is prime or not
def PrimeNum(n):
    i=1
    count=0
    while(i<=n):
        if(n%i==0):
            count=count+1
        i=i+1
    
    if(count==2):
        print(f'{n} is a prime number')
    else:
        print(f'{n} is not a prime')
        
w=int(input("Enter a number: "))
PrimeNum(w)