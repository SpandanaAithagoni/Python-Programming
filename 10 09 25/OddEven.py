def OddEven(list):
    oddC=0
    evenC=0
    for i in list:
        if(i%2==0):
            evenC=evenC+1
        else:
            oddC=oddC+1
    print("EvenCount=",evenC)
    print("OddCount=",oddC)
l1=[1,2,3,4,5,6,10]
OddEven(l1)
        