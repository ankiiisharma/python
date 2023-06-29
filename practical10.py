# Practical : 10
# Python program for SELECTION SORT.
# Name : Ankit Sharma
# Roll No. : 2100300100031 

def selsort(n):

    for i in range(len(n)-1,0,-1):

        max=0

        for j in range(1,i+1):

            if n[j]>n[max]:

                max = j

            temp = n[i]

            n[i] = n[max]

            n[max] = temp

n = [12,23,26,21,66,58,96,99]

selsort(n)

print("Sorted array : ",n)
