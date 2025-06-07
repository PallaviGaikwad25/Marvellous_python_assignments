def sumdigits(n):
    sum=0
    while n>0:
               
        sum=(n%10)+sum
        n=n//10
    print(sum)

def main():
    print("enter the number")
    no=int(input())
    sumdigits(no)

if __name__=="__main__":
    main()




def sumdigits(n):
    if n==0:
        return 0
    else:
        return (n%10)+sumdigits(n//10)      
        

def main():
    print("enter the number")
    no=int(input())
    res=sumdigits(no)
    print(res)
if __name__=="__main__":
    main()
