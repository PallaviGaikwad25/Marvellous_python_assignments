def chknum(no):
    if no % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

if __name__=="__main__":
    print("enter the number")
    num=int(input())
    chknum(num)