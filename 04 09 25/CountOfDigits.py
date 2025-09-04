#Print the number of digits in a number
def CountOfD(n):
    count=0
    while(n>0):
        n=n//10
        count=count+1
    return count

w=int(input("Enter a number: "))
print(CountOfD(w))
        