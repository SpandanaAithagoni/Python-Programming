def addEle(s1):
    n=int(input("No.of elements: "))
    for i in range(n):
        v=int(input("Enter the values: "))
        s1.add(v)
    
s2=set()
addEle(s2)
print(s2)