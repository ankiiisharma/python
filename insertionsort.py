a=[]

n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    a.append(ele)

print("Array without sorted is: ")
print(a)
b=[]

for i in range(1,len(a)):
    key = a[i]
    j = i-1  
    while j>0 and key<=a[j]:
        a[j+1]=a[j] 
        j = j-1  
        a[j+1] = key  
for i in a:  
    b.append(i) 
print("Elements in sorted order are:",b) 