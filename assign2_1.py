import Arithmatic1

def main():
    x=int(input("enter first number"))
    y=int(input("enter second number"))
    res=Arithmatic1.add(x,y)
    print("Addition :",res)
    res=Arithmatic1.sub(x,y)
    print("Substraction :",res)
    res=Arithmatic1.mul(x,y)
    print("Multiplication :",res)
    res=Arithmatic1.div(x,y)
    print("division :",res)
 

if __name__=="__main__":
    main()