# Practical : 10
# Python program for INSERTION SORT.
# Name : Ankit Sharma
# Roll No. : 2100300100031 

a=[5,7,13,21,23,55,43,98,21,46]

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


