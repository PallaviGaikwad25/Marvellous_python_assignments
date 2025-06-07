import threading
def small(s):
    count=0
    for ch in s:
        if  ch >= 'a' and ch <= 'z':
            count=count+1
    print("small letters=",count)
def capital(s):
    count=0
    for ch in s:
        if ch >= 'A' and ch <= 'Z':
            count=count+1
    print("Capital letters=",count)
    
def digits(s):
    count=0
    for i in s:
        if i>='0' and i <='9' :
            count=count+1 
    print("total digits=",count)

def main():
    data=list()
    print("how many elements in your data?")
    num=int(input())
    print("enter character,or digit")
    while len(data)<num:
        ch=input("Enter:")
        if len(ch)!=1:
            print("enter only one  character or digits")
            continue
        data.append(ch)
    print("user list",data)

    small_thread=threading.Thread(target=small,args=(data,))
    capital_thread=threading.Thread(target=capital,args=(data,))
    digits_thread=threading.Thread(target=digits,args=(data,))
     
    small_thread.start()
    capital_thread.start()
    digits_thread.start()
    small_thread.join()
    capital_thread.join()
    digits_thread.join()

if __name__=="__main__":
    main()
