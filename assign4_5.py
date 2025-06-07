from functools import reduce
data=[]
no=int(input("enter how any elements in list :="))
for i in range(1,no+1):
    num=int(input())
    data.append(num)
print(data)
def isprime(n):
    for j in range(2,n):
        if n %j==0:
            return False
    return True
def maxnum(n):
    max=n[0]
    for x in range(n):
        if max>n:
            max=n
    return max
filtered_list=list(filter(isprime,data))
print("list of prime numbers is:=",filtered_list)

maplist=list(map(lambda x :x*2,filtered_list))
print("multiplying each number by 2",maplist)

reducelist=reduce(maxnum,maplist)
print("additionof all numbers form : ",reducelist)


