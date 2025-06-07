from functools import reduce
data=[]
no=int(input("enter how any elements in list :="))
for i in range(1,no+1):
    num=int(input())
    data.append(num)
print(data)

filtered_list=list(filter(lambda x:x%2==0,data))
print("list after filter is:=",filtered_list)

maplist=list(map(lambda x :x*x,filtered_list))
print("sqaure of numbers from filtered list",maplist)

reducelist=reduce(lambda x,y:x+y,maplist)
print("additionof all numbers form : ",reducelist)


