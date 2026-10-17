# 3. Rotate Matrix 90° Anticlockwise
def rotateMatrix__(self,matrix):
    n=len(matrix)

    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        
  
    matrix.reverse()

    return matrix