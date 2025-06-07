def listcreate(no):
    data=list()
    print("enter elements")
    for i in range(1,no+1):
        no=int(input())
        data.append(no)

    print ("entered elements are")
    for value in data:
        print(value,end=" ")
    
    max=data[0] #assume first number is max for compare with other element in list
    for i in data:#loop to access elements 
        if i>max:
            max=i
    print("maximum number is",max)
def main():
    print("enter the elements")
    no1=int(input())
    listcreate(no1)
    

if __name__=="__main__":
    main()