class Solution(object):
    def isNumber(self, s):
        import re
        s = s.strip()
        if re.findall('^(\+|-)?((\d*\.?\d+)|(\d+\.?\d*))(e|E)(\+|-)?\d+$',s) or re.findall('^(\+|-)?((\d*\.?\d+)|(\d+\.?\d*))$',s):
            return True
        else:
            return False