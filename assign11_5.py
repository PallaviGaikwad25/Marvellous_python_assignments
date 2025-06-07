#count 0 in number

def countzero(no):
    count=0
    while no>0:
        digit=no%10
        if digit==0:
            count+=1
        no=no//10
    return count

def main():
    print("enter the number")
    no=int(input())
    res=countzero(no)
    print(res)

if __name__=="__main__":
    main()



#count o in number by recursion

def countzero(no,count=0):
    if no==0:
        if count > 0:
            return count
        else:
            return 1

    digit=no%10
    if digit==0:
        count+=1
    return countzero(no // 10,count)
       
    
def main():
    print("enter the number")
    no=int(input())
    res=countzero(no)
    print(res)

if __name__=="__main__":
    main()