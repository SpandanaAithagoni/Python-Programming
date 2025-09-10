def length(str):
    count=0
    for i in str:
        count=count+1
    return count

def compare(str1,str2):
    if(str1==str2):
        return True
    else:
        return False

def concat(str1,str2):
    return str1+str2

s1="HelloWorld"
s2="WaterPark"
print(length(s1))
print(length(s2))
print(compare(s1,s2))
print(concat(s1,s2))
        