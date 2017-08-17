class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a)
        if m<len(b):
            a='0'*(len(b)-len(a))+a
        if m>len(b):
            b='0'*(len(a)-len(b))+b
        re,c = '',0
        for i in range(m):
            tmp = int(a[-1-i])+int(b[-1-i])+c
            re = str(tmp%2)+re
            c = tmp/2
        return (c==1 and '1'+re or re)

print Solution().addBinary('1','1001')