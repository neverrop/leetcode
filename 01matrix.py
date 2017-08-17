class Solution(object):
    def updateMatrix(self,matrix):
        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0]!=0:
            matrix[0][0] = float('inf')

        for i in range(m):
            for j in range(n):
                if matrix[i][j]!=0 and (i!=0 or j!=0):
                    matrix[i][j] = min((i>0 and matrix[i-1][j]+1 or float('inf')), (j>0 and matrix[i][j-1]+1 or float('inf')))

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j] != 0 and (i != m-1 or j != n-1):
                    matrix[i][j] = min(min((i < m-1 and matrix[i + 1][j]+1 or float('inf')),
                                       (j < n-1 and matrix[i][j + 1]+1 or float('inf'))),matrix[i][j])
        return matrix

matrix = [[1,1,1],[1,0,0],[1,1,1]]
print Solution().updateMatrix(matrix)