#Check whether a number is palindrome or not
def palindrome(n):
    for i in range(1,n+1):
        y=str(i)
        z=y[::-1]
        if(y==z):
            print(i,end=" ")
        
w=int(input("Enter a number: "))
palindrome(w)