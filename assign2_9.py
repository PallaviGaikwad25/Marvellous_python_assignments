def digitscount(no):
    count=0
    while no>0:
        no=no//10
        count=count+1
    return count
    
def main():
    print("enter the number")
    no1=int(input())
    res=digitscount(no1)
    print("number of digits=",res)
if __name__=="__main__":
    main()
    
