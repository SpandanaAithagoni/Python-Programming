#Print prime numbers between 1 to n
def Prime1ToN(n):
    for i in range(2, n):  
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:  
            print(i, end=" ")

w = int(input("Enter a number: "))
Prime1ToN(w)
