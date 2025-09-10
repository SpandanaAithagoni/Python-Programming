def Count(str):
    dc=0
    cc=0
    sc=0
    for i in str:
        if i.isalpha():
            cc=cc+1
        elif i.isdigit():
            dc=dc+1
        else:
            sc=sc+1
    print("Alphabet count: ",cc) 
    print("Digit count: ",dc)
    print("Special Character count: ",sc)
    
    
S1="Hello@123"
Count(S1)
           