import threading
def thread1():
    print("enter 1 to 50 numbers")
    for i in range(1,51,1):
        print(i)
def thread2():
    print("enter reverse number")
    for i in range(50,0,-1):
        print(i)



def main():
    thread1_thread=threading.Thread(target=thread1)
    thread1_thread.start()
    thread1_thread.join()

    thread2_thread=threading.Thread(target=thread2)
    thread2_thread.start()
    thread2_thread.join()


if __name__=="__main__":
    main()