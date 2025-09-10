def AlphaOcc(strg):
    freq={}
    str2=" "
    for i in range(len(strg)):
        if strg[i] in freq:
            freq[strg[i]]+=1
        else:
            freq[strg[i]]=1
    for i in freq:
        str2+=i+str(freq[i])
    print(str2)

s1="HelloWorld"
AlphaOcc(s1)