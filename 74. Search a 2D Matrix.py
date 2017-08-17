class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l = self.bin([i[0] for i in matrix],target)
        if target == self.bin(matrix[l],target):
            return True
        else:
            return False

    def bin(self,s,k):
        l,r = 0,len(s)-1
        while l<r:
            if s[r]<=k:
                return r
            mid = (l+r)/2
            if k==s[mid]:
                return mid
            if k>s[mid]:
                l = mid+1
            else:
                h = mid-1
        return h-1
matrix = [[1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]]
print Solution().searchMatrix(matrix,3)

