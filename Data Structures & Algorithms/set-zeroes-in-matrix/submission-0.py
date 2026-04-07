class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        zeros=[]
        for r in range(m):
            for c in range(n):
                if matrix[r][c]==0:
                    zeros.append((r,c))
        for r, c in zeros:
            for j in range(n):
                matrix[r][j]=0
            for i in range(m):
                matrix[i][c]=0
        