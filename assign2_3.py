#program to caluculate factorial of number
def main():

    print("enter the number")
    x=int(input())
    res=1
    for i in range(1,x+1):
        res=res*i
    print(res)
if __name__=="__main__":
    main()
