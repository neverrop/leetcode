class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        re = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i==0 or (nums[i]!=nums[i-1]):
                l = len(re)
            re+=[j+[nums[i]] for j in re[(len(re)-l):]]
        return re

print Solution().subsetsWithDup([1,2,2])
