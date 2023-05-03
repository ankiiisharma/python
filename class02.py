a=int(input("Enter Elements"))
list=[]
while(n!=0)
item=int(input("Enter Element"))

list.append(item)
a=a-1
print("max term:" max(list))
print("min term:" min(list))
print("mean term:" sum(list))