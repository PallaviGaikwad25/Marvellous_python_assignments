def pattern(no):
    for i in range(no,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()


def main():
    print("enter number to print pattern")
    no1=int(input())
    res=pattern(no1)
    
    
if __name__=="__main__":
    main()