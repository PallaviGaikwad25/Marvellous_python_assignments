class demo:
    value=0 #class variable
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
    def fun(self):
       print("inside fun method")
       print("no1=",self.no1,"no2=",self.no2)


    def gun(self):
        print("inside gun method")
        print("no1=",self.no1,"no2=",self.no2)


obj1=demo(11,21)
obj2=demo(51,101)


obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()

