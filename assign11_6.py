# sum of first n Natural numbers
def sumofn(no):
    sum=0
    if  no>=1:
        for i in range(1,no+1):
            sum=sum+i
        return sum
            
def main():
    print("enter the number")
    num=int(input())
    res=sumofn(num)
    print("addition of natural numbers up to n:=",res)
    
if __name__=="__main__":
    main()




# sum of first n Natural numbers recursion

def sumofn(no):
    
    if no<=0:
        return 0
    else:
        return no + sumofn(no-1)
            
def main():
    print("enter the number")
    num=int(input())
    res=sumofn(num)
    print("addition of natural numbers up to n:=",res)
    
if __name__=="__main__":
    main()
