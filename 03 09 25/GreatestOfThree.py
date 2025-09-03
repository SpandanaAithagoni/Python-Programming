def GOfThree(a,b,c):
    if(a>b):
        if(a>c):
            print(a," is greater")
    else:
        if(b>a and b>c):
            print(b," is greater")
        else:
            print(c," is greater")

p=int(input("Enter n1: "))
q=int(input("Enter n2: "))
r=int(input("Enter n3: "))
GOfThree(p,q,r)