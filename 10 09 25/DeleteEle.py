def DelEle(k,list):
    NList=[]
    for i in range(len(list)):
        if(i!=k):
            NList=NList+[list[i]]
    print(NList)
l1=[0,1,2,3,4]
DelEle(2,l1)