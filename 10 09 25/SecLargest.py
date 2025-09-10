def SecLar(list):
    min=list[0]
    sec=min
    for i in list:
        if i>min:
            min=i
    for i in list:
        if i!=min:
            if i>sec:
                sec=i
        
    return sec
l1=[0,4,38,7]
print(SecLar(l1))
        
    