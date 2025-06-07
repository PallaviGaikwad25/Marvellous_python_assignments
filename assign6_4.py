def main():
    print("enter the number")
    num=int(input())
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of number is",fact)

if __name__=="__main__":
    main()