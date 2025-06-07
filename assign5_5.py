#odd even check
def oddevenchk(num):
    if(num%2==0):
        return "even"
    else:
        return "odd"
def main():
    print("enter the number")
    no=int(input())
    res=oddevenchk(no)
    print("number is ",res)
if __name__=="__main__":
    main()