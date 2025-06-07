def chkprime(no):
    for i in range(2,no):
        if (no%i==0):
            return "number is not prime"
        else:
           return "number is prime"
def main():
    print("enter the number")
    num=int(input())
    res=chkprime(num)
    print(res)

if __name__ =="__main__":
    main()