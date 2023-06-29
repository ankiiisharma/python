# Practical : 6:
# Python program to find the exponentiation of a number
# Name : Ankit Sharma
# Roll No. : 2100300100031

num=int(input("Enter number: "))

exp=int(input("Enter exponential value: "))

result=1

for i in range(1,exp+1):

    result=result*num

print("Result is:",result)


