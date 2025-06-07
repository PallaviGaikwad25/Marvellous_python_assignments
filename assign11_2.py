def factno(n):
    fact=1
    for i in range(1,n+1,1):
        fact=fact*i
      
    print(fact)
def main():
    print("enter the numbers")
    no=int(input())
    factno(no)


if __name__=="__main__":
    main()



def factno(n):
    if n==1:
        return 1
    else:
        return n*factno(n-1)
      
def main():
    print("enter the numbers")
    no=int(input())
    res=factno(no)
    print(res)


if __name__=="__main__":
    main()