import threading
def evenlist(data1):
    sum=0
    for i in data1:
        if i%2==0:
            sum=sum+i
    print("addition of sum",sum)

def oddlist(data1):
    sum=0
    for i in data1:
        if i%2!=0:
            sum=sum+i
    print("addition of odd",sum)

def main():
    data=list()
    print("how many elements in list?")
    no=int(input())
    for i in range(1,no):
        num=int(input())
        data.append(num)
    print(data)

    evenlist_thread=threading.Thread(target=evenlist,args=(data,))
    oddlist_thread=threading.Thread(target=oddlist,args=(data,))

    evenlist_thread.start()
    oddlist_thread.start()

    evenlist_thread.join()
    oddlist_thread.join()

if __name__=="__main__":
    main()