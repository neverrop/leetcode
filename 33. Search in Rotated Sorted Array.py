class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)-1
        found = -1
        while l<=r and found==-1:
            while l<r and nums[l]==nums[r]:
                l+=1
            mid = (l+r)/2
            print nums[mid]
            if target == nums[mid] or target==nums[r]:
                found = mid

            if target< nums[mid]:
                if nums[mid]<nums[l]:
                    r=mid-1
                else:
                    if target>=nums[l]:
                        r=mid-1
                    else:
                        l=mid+1
            else:
                if nums[mid]>=nums[l]:
                    l=mid+1
                else:
                    if target>=nums[l]:
                        r=mid-1
                    else:
                        l=mid+1
        return found

print Solution().search([1,1,3,1],3)