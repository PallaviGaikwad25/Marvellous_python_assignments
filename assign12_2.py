class circle:
    pi=3.14
    def __init__(self):
       
        self.radius=0.0
        self.area=0.0
        self.circumference=0.0
    
    def accept(self):
        print("enter the radius")
        self.radius=float(input())

    def calculatearea(self):
        self.area=circle.pi*self.radius*self.radius

    def calculatecircumference(self):
        self.circumference=2*circle.pi*self.radius

    def display(self):
        print("enter radius",self.radius)
        print("circle area",self.area)
        print("circumference of circle",self.circumference)
def main():
    obj1=circle()
    obj1.accept()
    obj1.calculatearea()
    obj1.calculatecircumference()
    obj1.display()

if __name__=="__main__":
    main()
