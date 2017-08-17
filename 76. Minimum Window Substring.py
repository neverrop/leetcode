class Solution(object):
    def minWindow(self, s, t):
        import collections
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need,left = collections.Counter(t),len(t)
        i,I,J = 0,0,0
        for j,c in enumerate(s,1):
            left -= (need[c]>0)
            need[c]-=1
            if not left:
                while i<j and need[s[i]]<0:
                    need[s[i]]+=1
                    i+=1
                if not J or j-i<J-I:
                    I,J = i,j
        return s[I:J]
