def printno(n):
    for i in range(1,n+1,1):
      
      print(i)
def main():
    print("enter the numbers")
    no=int(input())
    printno(no)


if __name__=="__main__":
    main()



def printno(n):
    if n == 0:
        return
    printno(n - 1)  
    print(n)        

def main():
    print("Enter the number:")
    no = int(input())
    printno(no)

if __name__ == "__main__":
    main()