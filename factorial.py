def factorial(n):
    if n==1:
        return n
    else:
       return n*factorial(n-1)

num = int(input("Enter Number: "))

if num < 0:
    print("Factorial does not exists for negative number")

elif num==0:
    print("Factorial of 0 is 1")

else:
    print("Factorial of",num,"is : ", factorial(num))