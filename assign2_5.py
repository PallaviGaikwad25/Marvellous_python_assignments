def prime(no):
    if no<=1:
        return False
    for i in  range(2,no):
        if no % i==0:
            return False
    else:
        return True

def main():
    print("enter number")
    no1=int(input())
    res=prime(no1)
    if res==True:
        print("number is   prime")
    else:
        print("number is not prime")

    
if __name__=="__main__":
    main()