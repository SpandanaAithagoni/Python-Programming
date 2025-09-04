#Print pattern
def p2(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==j):
                print("$",end=" ")
            else:
                print("*",end=" ")
                
        print()
w=int(input("Enter a number for pattern: "))
p2(w)