#Power function 
def powerrec(no,no1):
    ans=1
    count=0
    while(count<no1):
        ans=ans*no
        count+=1
      
    return ans
       

def main():
    print("enter first number")
    num=int(input())
    print("enter second number")
    num1=int(input())
    res=powerrec(num,num1)
    print(res)

if __name__=="__main__":
    main()

#using recusion 
def powerrec(no,no1):
    if no1==0:
        return 1
    return no*powerrec(no,no1-1)

def main():
    print("enter first number")
    num=int(input())
    print("enter second number")
    num1=int(input())
    res=powerrec(num,num1)
    print(res)

if __name__=="__main__":
    main()