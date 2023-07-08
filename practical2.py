# Practical : 2 :
# to perform matrix multiplication!
# Name : Ankit Sharma
# Roll No. : 2100300100031

A = [[3, 2, 2],
    [4, 1, 6],
    [7, 6, 4]]
 
B = [[4, 7, 1, 2],
    [2, 7, 3, 0],
    [4, 5, 4, 2]]
     
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
 
for r in result:
    print(r)


