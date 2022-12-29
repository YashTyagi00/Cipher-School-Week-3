class Employee:
    increment = 1.5
    no_of_employe= 0
    def __init__(self,fname,lname,salary):  
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=1.4
        Employee.no_of_employe +=1
 
    def increase(self):
        self.salary = int(self.salary * Employee.increment)
 
    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount








class Programmer(Employee):
    pass
harry = Programmer("harry","jackson",99000)
print(harry.fname)
print(harry.lname)
print(harry.salary)