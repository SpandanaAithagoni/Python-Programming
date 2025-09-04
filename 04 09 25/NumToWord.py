#Convert a digit into words
def NumToWord(n):
    digits=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    res=0
    for i in str(n):
        print(digits[int(i)],end=" ")
w=int(input("Enter a number: "))
NumToWord(w)