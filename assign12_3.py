class arithmetic:
    def __init__(self):
        self.value1=0.0
        self.value2=0.0
        
       
    def accept(self):
        print("enter value1 and value2")
        self.value1=int(input())
        self.value2=int(input())

    def addition(self):
        return self.value1+self.value2

    def substraction(self):
          return self.value1-self.value2

    def multiplication(self):
          return self.value1*self.value2

    def division(self):
        if self.value2==0:
            print("we cannot divide number by zer0")
        else:

            return self.value1/self.value2
 

def main():
    obj1= arithmetic()
    obj1.accept()
    add=obj1.addition()
    sub=obj1.substraction()
    mul=obj1.multiplication()
    div=obj1.division()
    print("addition is",add)
    print("substraction",sub)
    print("multiplication",mul)
    print("division",div)

    
if __name__=="__main__":
   main()   

    