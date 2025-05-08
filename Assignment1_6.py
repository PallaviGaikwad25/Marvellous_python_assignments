def chknum(no):
    if no == 0:
        print("number is Zero")
    elif no> 0:
        print("Number Is Positive")
    else:
        print("number is negavtive")


if __name__=="__main__":
        print("enter the number")
        n=int(input())
        chknum(n)