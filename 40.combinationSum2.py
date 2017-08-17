class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.com(candidates,target,[],[])

    def com(self,candidates,target,re = [],r = []):
        if target==0:
            re.append(r)
            return
        for i in xrange(len(candidates)):
            if candidates[i]>target:
                break
            if i>0 and candidates[i] == candidates[i - 1]: continue
            self.com(candidates[(i+1):],target-candidates[i],re,r+[candidates[i]])
        return re

a = Solution()
print a.combinationSum2([1],1)
