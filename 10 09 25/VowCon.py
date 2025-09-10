def Count(str):
    vowels=['a','e','i','o','u']
    vc=0
    cc=0
    for i in str:
        if i.isalpha():
            if i in vowels:
                vc+=1
            else:
                cc+=1
    print("Vowel count: ",vc)
    print("Consonant count: ",cc)

s1="HappyBirthday"
Count(s1)
