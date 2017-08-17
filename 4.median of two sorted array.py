def findMedianSortedArrays(nums1, nums2):
    if (not nums1) and (not nums2):
        return 0
    i = 0
    l1 = len(nums1)
    l2 = len(nums2)
    while i < (l1+l2)/2 + 1 :
        if nums1 and nums2:
            curr = nums1[0]<nums2[0] and nums1.pop(0) or nums2.pop(0)
        else:
            curr = nums1 and nums1.pop(0) or nums2.pop(0)
        re = i==(l1+l2)/2.0 and (re+curr)/2.0 or curr
        print i,re,curr
        i+=1
    return re
print findMedianSortedArrays([1],[4,6,8])