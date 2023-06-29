# Practical : 3 :
# Program to find gcd of two numbers
# Name : Ankit Sharma
# Roll No. : 2100300100031
def gcd(a,b):

    if(b==0):

        return a

    else:

        return gcd(b,a%b)

a=int(input("Enter first number:"))

b=int(input("Enter second number:"))

GCD=gcd(a,b)

print("GCD of ",a," and ",b,"is:",GCD)