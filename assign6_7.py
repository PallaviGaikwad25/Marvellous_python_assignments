def chkmax(data):
    max1=data[0]
    for i in data:
        if i>max1:
            max1=i
    return max1
        

def main():
    data1=list() # create empty list
    print("enter 5 elements in list")
    for i in range(1,6):
        num1=int(input())
        data1.append(num1)
        print(data1) 
    res=chkmax(data1)
    print("maximum number from list:=",res)
if __name__=="__main__":
    main()
    
        