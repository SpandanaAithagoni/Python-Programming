def Div(a):
    if(a%5==0  and a%11==0):
        print("Divisible by both 5 and 11")
    else:
        print("Not divisible by 5 and 11")

q=int(input("Enter a number: "))
Div(q)
