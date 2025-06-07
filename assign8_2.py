import threading
def evenfactor(no):
    sum=0
    for i in range(2,no+1,2):
        sum=sum+no
    print("evenfactor",sum)

def oddfactor(no):
    sum=0
    for i in range(1,no+1,2):
       
            sum=sum+no
    print("oddfactor",sum)

def main():
    print("enter number")
    no1=int(input())

    even_thread=threading.Thread(target=evenfactor(no1))

    odd_thread=threading.Thread(target=oddfactor(no1))

    even_thread.start()

    odd_thread.start()

    even_thread.join()
    odd_thread.join()
    print("exit from main")


if __name__=="__main__":
    main()