def freqEle(list):
    freq={}
    for i in range(len(list)):
        if list[i] in freq:
            freq[list[i]]+=1
        else:
            freq[list[i]]=1
    for i in freq:
        print(f'{i}->{freq[i]}')
l1=[2,3,3,4,5,6,3,7,9,6]
freqEle(l1)