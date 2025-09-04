#Print the multiplication table of a number
def MulTable(n):
    for i in range(1,11):
        print(n,'*',i,'=',n*i)

w=int(input("Enter a number: "))
MulTable(w)
        
        