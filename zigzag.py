def convert(s,numRows):
    re = ''
    for i in range(numRows):
        r = ''
        for j in range(i,len(s),2*(numRows-1)):
            r+=s[j]
            if (0< 2*(numRows-i-1) < i+2*(numRows-1)) and ((j+ 2*(numRows-i-1))<len(s)):
                r+=s[j+ 2*(numRows-i-1)]
        re+=r
    return re

print convert('PAYPALISHIRING',3)