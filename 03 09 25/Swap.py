#Swapping two numbers
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Before swapping: a=",a, "b=",b)
'''c=a
a=b
b=c'''
a,b=b,a
print("After swapping: a=",a, "b=",b)