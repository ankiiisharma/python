# Practical : 8:
# Python Progarm to perform Linear Search.
# Name : Ankit Sharma
# Roll No. : 2100300100031

def search(list,n):  

    for i in range(len(list)): 

        if list[i] == n: 

            return True

    return False 

list = [1, 2, 'goeduhub', 4,'python','machine learning',6]  

n = 'python'

if search(list, n): 

    print("Found at index ",list.index(n)) 

else: 

    print("Not Found")

