list = [1,2,3]

avg = 0
sum = sum(list)
length = len(list)

try:
    avg = sum/length

except ZeroDivisionError as e:
    print("Division by Zero is not possibe")

print(avg)