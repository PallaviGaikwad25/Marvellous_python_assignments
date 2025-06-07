def listcreate(no):
    data=list()
    print("enter elements")
    for i in range(1,no+1):
        no=int(input())
        data.append(no)

    print ("entered elements are")
    for value in data:
        print(value,end=" ")
    
    min=data[0]
    for i in data:
        if i<min:
            min=i
    print("minimum number is",max)
def main():
    print("enter the elements")
    no1=int(input())
    listcreate(no1)
    

if __name__=="__main__":
    main()