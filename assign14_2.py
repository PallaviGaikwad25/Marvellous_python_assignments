class Rectangle:
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid
       

    def area(self):
        return self.len*self.wid



    def perimeter(self):
        return 2*(self.len+self.wid)
    


def main():
    print("enter length")
    l=float(input())
    print("enter width")
    w=float(input())
    obj1=Rectangle(l,w)
    print("Area of Recttrianle is==",obj1.area())
    print("Perimeter of rectangle",obj1.perimeter())

    
if __name__=="__main__":
        main()