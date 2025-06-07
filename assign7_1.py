
def main():

    square=lambda x:x*x

    cube=lambda x:x*x*x

    print("enter the number")
    x=int(input())
    print("sqaure of number",square(x))
    print("sqaure of number",cube(x))

if __name__=="__main__":
    main()