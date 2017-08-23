class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1 + s2) != len(s3):
            return False
        stack, visited = [(0,0)],set((0,0))
        while stack:
            x,y = stack.pop()
            if x+y == len(s3):
                return True
            if x+1<= len(s1) and s1[x] == s3[x+y] and (x+1,y) not in visited:
                stack.append((x+1,y))
                visited.add((x+1,y))
            if y+1<= len(s2) and s2[y] == s3[x+y] and (x,y+1) not in visited:
                stack.append((x,y+1))
                visited.add((x,y+1))
        return False

print Solution().isInterleave('11','2','121')
# print Solution().isInterleave('aabcc','dbbca',"aadbbcbcac")
