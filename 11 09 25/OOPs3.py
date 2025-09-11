from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        Ar=self.l*self.b
        print("Area of the rectangle: ",Ar)
        
class circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        Ac=math.pi*self.r*self.r
        print("Area of circle: ",Ac)

r1=rectangle(5,6)
r1.area()
c1=circle(10)
c1.area()
    