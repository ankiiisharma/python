# Practical : 4:
# Python program to find the most frequent words in a text read from a file
# Name : Ankit Sharma
# Roll No. : 2100300100031

file__IO ="C:\\Users\\siddh\\Desktop\\hello World\\python\\python.txt" 

with open(file__IO, 'r') as f:

    data = f.read()

    line = data.splitlines()

    words = data.split()

    spaces = data.split(" ")

    charc = (len(data) - len(spaces))

print('\n Line number:', len(line), '\n Words number:', len(words), '\n Spaces:', len(spaces), '\n Characters:', (len(data)-len(spaces)))



