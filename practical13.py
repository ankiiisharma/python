# Practical : 13
# Python program to find first n prime numbers
# Name : Ankit Sharma
# Roll No. : 2100300100031 

numr=int(input("Enter range:"))

print("Prime numbers:",end=' ')

for n in range(1,numr):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n,end=' ')    

