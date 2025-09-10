def RemDuplicates(list):
    dict={}
    list2=[]
    for i in list:
        if i not in dict:
            dict[i]=True
            list2+=[i]
    print(list2)    
l1=[2,3,3,4,5,6,3,7,9,6]
RemDuplicates(l1)