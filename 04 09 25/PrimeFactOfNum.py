def PrimeNum(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count == 2

def PrimeFactors(n):
    for i in range(2, n + 1):
        if n % i == 0 and PrimeNum(i):
            print(i, end=" ")
PrimeFactors(10)
