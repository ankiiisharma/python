# def show_excitement():
#     # Your code goes here!
#     string="I am super excited for this course! " *5 
#     return string

# print show_excitement()


def add():
    ans=num1+num2
    return ans
# print (add())

def sub():
    ans=num1-num2
    return ans
# print (sub())

def mul():
    ans=num1*num2
    return ans
# print(mul())

def div():
    ans=num1/num2
    return ans
# print(div())


num1=int(input("Enter Number 1 :  "))
num2=int(input("Enter Number 2 :  "))

print ("Select the operation you eant to perform")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")

ops = int(input("Enter here:  "))

if(ops==1):
    print(add())

elif(ops==2):
    print(sub())

elif(ops==3):
    print(mul())

elif(ops==4):
    print(div())

else:
    print("WRONG CHOICE!")






