def main():
    data=list()
    print("enter number of elements in list")
    num=int(input())
    for i in range(num):
        value=int(input())
        data.append(value)
    print(data)

    filter1=list(filter(lambda x:x%2==0,data))
    print("even number in list",filter1)



if __name__=="__main__":
    main()