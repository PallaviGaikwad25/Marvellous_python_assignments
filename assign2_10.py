def digitscount(no):
    sum=0
    while no>0:
        digit=no % 10 #for digit seperation  
        sum=sum+digit
        no=no//10 #for removing last digit
        

    return sum
    
def main():
    print("enter the number")
    no1=int(input())
    res=digitscount(no1)
    print("number of digits=",res)
if __name__=="__main__":
    main()
    
