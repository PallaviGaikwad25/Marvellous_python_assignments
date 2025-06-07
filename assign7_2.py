def main():

    data=list()
    print("enter the number")
    num=int(input())
    for i in range(num):
        value=int(input())
        data.append(value)
    print(data)
    mapfunction=list(map(lambda x:x*2,data))
    print(mapfunction)


if __name__=="__main__":
    main()