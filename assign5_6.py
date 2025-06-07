#celsius to fahrenheit check
def chktemp(c):
    temp= (c*9.5)+32
    return temp


def main():
    print("enter the temperature ")
    temp1=float(input())
    res=chktemp(temp1)
    print(f" tempreature in fahrenheit {res} F")



if __name__=="__main__":
    main()