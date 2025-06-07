import MarvellousNum

def listprime(no):
    data=list()
    print("list elements")
    for i in range(1,no+1):
        no=int(input())
        data.append(no)
    print("entered element is")

    
    for value in data:
        print(value,end=" ")
    primesum=0
    for no in data:
        if MarvellousNum.chkprime(no):
            primesum=primesum+no
    def main():
        print("enter how many elemnets to list")
        n=int(input())
        res=listprime(n)
    if __name__=="__main__":
        listprime()