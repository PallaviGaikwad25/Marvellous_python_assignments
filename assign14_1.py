class employee:
    def __init__(self,name,empid,salary):
        self.name=name
        self.empid=empid
        self.salary=salary

name1=input("enter your name")
id=int(input("enter employee id"))
sal=float(input("enter salary"))


p1=employee(name1,id,sal)
print("employee name=",p1.name)
print("employee id=",p1.empid)
print("employee salary=",p1.salary)