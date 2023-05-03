# # program to calculate income tax of an employee on the basis of base salary and toatal savings inputed by the user. using nested if else as per given table
# 1. No Tax for income less than 2,50,500.
# 2. 5% tax with income Rs. 2,50,00 to 5,00,000
# 3. 20% tax with income Rs. 5,00,000 to Rs. 10,00,000.
# 4. 30% tax with income over Rs 10,00,000





s=int(input("Enter Your Salary \n"))
i=int(input("Enter Investments\n"))

if(s>500000):
    temp=((20/100)*s)
    print(temp)

    if(i>150000):
        print("tax is:")
        print(temp-45000)