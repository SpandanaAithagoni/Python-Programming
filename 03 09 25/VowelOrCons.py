def VowelOrCons(a):
    return(a=='a' or a=='e'or a=='i' or a=='o' or a=='u')
k=input().lower()
if VowelOrCons(k):
    print(f'{k} is an vowel')
else:
    print(f'{k} is a consonant')