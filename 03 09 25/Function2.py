#Function with args list and no return
#convert days to years and months
def days(x):
    y=x/365
    m=x/30
    print("Years: ",round(y,2),"Months: ",round(m,2))

x=int(input())
days(x)