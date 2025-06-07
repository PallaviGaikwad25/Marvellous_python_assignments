from functools import reduce
data=[]
no=int(input("enter how any elements in list"))
for i in range(1,no+1):
    num=int(input())
    data.append(num)
print(data)

filtered_list=list(filter(lambda x:x>=70 and x<=90 ,data))
print("list after filter is:=",filtered_list)

maplist=list(map(lambda x :x+10,filtered_list))
print("list after map",maplist)

reducelist=reduce(lambda x,y:x*y,maplist)
print("list ouput after reduce",reducelist)


