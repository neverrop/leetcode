class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        re = []
        self.solve(n,re,0,[],[],[])
        return [['.'*i+'Q'+'.'*(n-i-1) for i in  sol] for sol in re]

    def solve(self,n,re,i,ro,l,r):
        if i==n:
            re.append(ro)
            return
        for j in range(n):
            if (j not in ro) and ((j-i) not in r) and ((j+i) not in l):
                self.solve(n,re,i+1,ro+[j],l+[i+j],r+[j-i])

print Solution().solveNQueens(4)