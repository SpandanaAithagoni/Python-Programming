#Print pattern 
def p1(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*",end=" ")
        print()
        
w=int(input("Enter a number for pattern: "))
p1(w)