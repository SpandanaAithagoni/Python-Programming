def StrongNum(n):
    for num in range(1, n + 1):
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            fact = 1
            for j in range(1, digit + 1):
                fact *= j
            sum+= fact
            temp=temp//10
        if sum == num:
            print(num, end=" ")

w = int(input("Enter the range: "))
StrongNum(w)
