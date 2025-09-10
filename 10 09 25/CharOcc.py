def CharOcc(x,str):
    
    for i in range(len(str)):
        if str[i]==x:
            print(i,end=" ")

s1="HappyBirthday"
CharOcc('a',s1)