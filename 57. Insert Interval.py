class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s,e = newInterval.start,newInterval.end
        l,r = [],[]
        for i in intervals:
            if i.end<s:
                l.append(i)
            elif i.start>e:
                r.append(i)
            else:
                s = min(i.start,s)
                e = max(i.end,e)
        return l+[Interval(s,e)]+r
a =  Solution().insert([Interval(1,3),Interval(6,9)],Interval(2,5))
print a