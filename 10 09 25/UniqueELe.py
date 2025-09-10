def Unique(list):
    freq={}
    for i in range(len(list)):
        if list[i] in freq:
            freq[list[i]]+=1
        else:
            freq[list[i]]=1
            
    for i in freq:
        if(freq[i]==1):
            print(i)
l1=[2,3,3,4,5,6,3,7,9,6]
Unique(l1)