matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

# for i in range(len(matrix)):
#     for j in range(len(matrix[0]))

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if j==i:
    


# n=int(input("Enter number of rows:"))
# m=int(input("Enter number of columns:"))

# matrix=[]

# for i in range(n):
#     row=[]
#     for j in range(m):
#         num=int(input())
#         row.append(num)
#     matrix.append(row)

# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j],end=" ")
#     print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = len(matrix)

for i in range(n):
    print(matrix[i][n - 1 - i], end=" ")