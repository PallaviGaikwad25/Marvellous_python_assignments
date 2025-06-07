def pattern(no):
    for i in range(1,no+1,1):
        for j in range(1,no+1,1):
            print(j,end=" ")
        print()


def main():
    print("enter number to write pattern")
    no1=int(input())
    res=pattern(no1)

if __name__=="__main__":
    main()