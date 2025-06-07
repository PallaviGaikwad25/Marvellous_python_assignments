#area and perimeter of rectangle
def arearect(l,w):
    area=l*w
    return area
def perirect(l,w):
    perimeter=2*(l+w)
    return perimeter
def main():
    print("enter length and width")
    l1=int(input())
    w1=int(input())
    res=arearect(l1,w1)
    res1=perirect(l1,w1)
    print("Area of reactanle is",res)
    print("Area of reactanle is",res1)
if __name__=="__main__":
    main()
    
