def listcreate(no):
    data=list()
    print("list elements")
    for i in range(1,no+1):
        no=int(input())
        data.append(no)
    print("entered element is")
    for value in data:
        print(value,end=" ")
    print("enter number ")
    n=int(input())
    count=0
    for j in data:
        if n==j:
            count+=1
    print("frequency of elemnet is",count)

    
def main():
    print("enter number of elements ")
    num=int(input())
    res=listcreate(num)
 
if __name__=="__main__":
    main()