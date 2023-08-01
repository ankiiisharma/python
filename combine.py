list1 = [1,2,3]
list2 = [4,5,6]

count=0
x=len(list1)


while count<=x:
    for i in list1:
        for j in list2:

            print(i,j)
            count=count+1