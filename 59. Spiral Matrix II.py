class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = [[0]*n for _ in range(n)]
        self.gene(m,n,0,1)
        return m

    def gene(self,m,n,i,st):
        nn = n-2*i
        if nn==0:
            return m
        if nn==1:
            m[i][i] = st
            return m
        m[i][i:(-i-1)] = range(st,st+nn-1)
        for j in range(i,i+nn-1):
            m[j][i+nn-1]=st+nn-1+j-i
        m[-i-1][(i+1):(i+nn)] = range(st+3*nn-4,st+2*nn-3,-1)
        for j in range(i+1,i+nn):
            m[j][i] = st+4*nn-5 + i+1-j
        self.gene(m,n,i+1,st+4*nn-4)

m= Solution().generateMatrix(9)
for i in m:
    print i