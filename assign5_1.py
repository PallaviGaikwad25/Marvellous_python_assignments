def Arithematic(no1,no2):
    ans=no1+no2
    ans1=no1-no2
    ans2=no1*no2
    try:
        ans3=no1/no2
    except ZeroDivisionError:
        ans3 = "Division by zero error"
    return ans,ans1,ans2,ans3

def main():
    try:

        print("enter two numbers")
        value1=int(input())
        value2=int(input())
        ret=Arithematic(value1,value2)
        print("Addition:",ret[0])
        print("substraction",ret[1])
        print("multiplication:",ret[2])
        print("division",ret[3])
    except ValueError:
        print("invalid input")


if __name__=="__main__":

    main()