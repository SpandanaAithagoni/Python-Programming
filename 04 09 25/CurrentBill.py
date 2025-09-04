#Calculate the current bill
def CBill(n):
    if(n<=50):
        print(n*3.80)
    elif(n>50 and n<=100):
        print((50*3.80)+((n-50)*4.20))
    elif(n>100 and n<=200):
        print((50*3.80)+(50*4.20)+((n-100)*5.10))
    elif(n>200 and n<=300):
        print((50*3.80)+(50*4.20)+(100*5.10)+((n-200)*6.30))
    elif(n>300):
        print((50*3.80)+(50*4.20)+(100*5.10)+(100*6.30)+((n-300)*7.50))
    else:
        print("Invalid")


k=int(input("No.of units used: "))
CBill(k)