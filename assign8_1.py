import threading

def evennum():
    
    for i in range(2,21,2):
        print("even",i)

def oddnum():
   
    for i in range(1,20,2):
        print("odd",i)

def main():
  
    even_thread=threading.Thread(target=evennum)
    odd_thread=threading.Thread(target=oddnum)
    even_thread.start()
    odd_thread.start()
    even_thread.join()
    odd_thread.join()

if __name__=="__main__":
    main()


