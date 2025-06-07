
#pattern 
def pattern(no):
    for i in range(1,no):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

def main():
    print("enter the number")
    no1=int(input())
    pattern(no1)

if __name__=="__main__":
    main()  


#pattern recurssion unable to code
