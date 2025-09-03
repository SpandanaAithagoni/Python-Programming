#Area and perimeter of circle and rectangle
r=int(input("Radius of circle: "))
l=int(input("Length of rectangle: "))
b=int(input("Breadth of rectangle: "))
pi=3.14
areaC=pi*r*r
areaR=l*b
perC=2*pi*r
perR=2*(l+b)
print("Rectangle: Area=",areaR, "Perimeter=",perR)
print("Circle: Area=",areaC, "Perimeter=",perC)