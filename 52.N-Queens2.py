class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.re = 0
        self.solve(n, 0, [], [], [])
        return self.re

    def solve(self, n, i, ro, l, r):
        if i == n:
            self.re += 1
            return
        for j in range(n):
            if (j not in ro) and ((j - i) not in r) and ((j + i) not in l):
                self.solve(n, i + 1, ro + [j], l + [i + j], r + [j - i])

print Solution().totalNQueens(4)