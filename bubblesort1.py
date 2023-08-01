def bubbleSort(array, size):


arr=[]

n=int(input("Enter Number of elements:\n"))
for i in range(0,n):
    element = int(input())
    arr.append(element)

print("\n Array Without sorting is: ")
print(arr)
size=len(arr) #length of our array

bubbleSort(arr, size)