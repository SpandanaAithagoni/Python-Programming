def WCount(str):
    wc=1
    for i in str:
        if i==" ":
            wc+=1
    print("No.of words: ",wc)

s1="Computer  Science Engineering"
WCount(s1)