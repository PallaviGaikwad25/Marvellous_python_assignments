
import threading
import time
def displaynum(t):
    for i in range(1,6):
        print(t+":",i)
        time.sleep(1)
def main():
    t1=threading.Thread(target=displaynum,args=("t1",))
    t2=threading.Thread(target=displaynum,args=("t2",))
    t3=threading.Thread(target=displaynum,args=("t3",))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__=="__main__":
    main()
    