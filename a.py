n = int(raw_input())
re = 0
m1 = [0]*n
m2 = [0]*n
m3 = [0]*(2*n)
m4 = [0]*(2*n)
for i in range(n):
    (x, y) = (int(x) for x in raw_input().split())
    re += m1[x]
    m1[x] +=1
    re +=m2[y]
    m2[y] +=1
    re += m3[x + y]
    m3[x + y] +=1
    re += m4[y - x+n];
    m4[y-x+n] +=1;
print re