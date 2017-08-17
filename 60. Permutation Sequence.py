class Solution(object):
    def getPermutation(self, n, k):
        import math
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        a = range(1,n+1)
        re = ''

        for i in range(n):
            s = min(k/(math.factorial(n-i-1)),(k-1)/(math.factorial(n-i-1)))
            re += str(a[s])
            a.remove(a[s])
            k = k%(math.factorial(n-i-1))
        return re

print Solution().getPermutation(4,1)