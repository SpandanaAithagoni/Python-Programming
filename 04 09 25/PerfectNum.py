#Print perfect numbers in a range
def PerNum(n):
    for i in range(1,n+1):
        temp=i
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum=sum+j
        if(sum==i):
            print(sum,end=" ")

q=int(input("Enter the range: "))
PerNum(q)