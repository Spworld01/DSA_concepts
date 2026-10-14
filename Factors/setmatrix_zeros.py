class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    self.markinfinity__(matrix,i,j)
                    

        for i in range(r):
            for j in range(c):
                if matrix[i][j]==float("inf"):
                    matrix[i][j]=0

        return matrix

    def markinfinity__(self,matrix,row,col):
        r=len(matrix)
        c=len(matrix[0])

        for i in range(c):
            if matrix[row][i]!=0:
                matrix[row][i]=float("inf")

        for j in range(r):
            if matrix[j][col]!=0:
                matrix[j][col]=float("inf")

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None: 
        r=len(matrix)
        c=len(matrix[0])

        rowtrack=[0 for _ in range(r)]
        coltrack=[0 for _ in range(c)]

        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rowtrack[i]=-1
                    coltrack[j]=-1

        for i in range(0,r):
            for j in range(0,c):
                if rowtrack[i]==-1 or coltrack[j]==-1:
                    matrix[i][j]=0
        
        return matrix
