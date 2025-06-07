def listcreate(no):
    data=list()
    print("enter elements")
    for i in range(1,no+1):
        no=int(input())
        data.append(no)

    print ("entered elements are")
    for value in data:
        print(value,end=" ")
    sum=0
    for j in data:
        sum=sum+j
    print("addition is",sum)
def main():
    print("enter the elements")
    no1=int(input())
    listcreate(no1)
    

if __name__=="__main__":
    main()