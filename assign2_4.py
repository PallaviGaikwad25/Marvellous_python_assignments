def factadd(no):
    
    res=0
    for i in range(1,no):#starts from 1 and exclude x 
        if no%i==0:#
            res=res+i
    print(res)

def main():
    print("enter number")
    x=int(input())
    res1=factadd(x)
    print("addition of factorial is",res1)
if __name__=="__main__":
    main()
