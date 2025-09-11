class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def display(self):
        print(self.name)
        print(self.salary)
        
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
        
    def display(self):
        super().display()
        print(self.department)
        
        
s1=Employee("Naksh",250000)
s1.display()
s2=Manager("Nayan",200000,"CSE")
s2.display()