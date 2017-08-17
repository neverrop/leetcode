n = int(raw_input())
r = 0
a = [0]*n
b = [0]*n
for i in range(n):
    (a[i], b[i]) = (int(x) for x in raw_input().split())
t = (sum(a) + sum(b))/(2*n)
for i in range(n-1):
    if (a[i]-t)*(b[i]-t) >0:
        r+=abs(a[i]+b[i]-2*t)
        a[i+1] += a[i] -t
        b[i+1] += b[i] -t
    else:
        if abs(a[i]-t)>abs(b[i]-t):
            a[i+1]+=a[i] + b[i] - 2*t
        else:
            b[i+1]+=b[i]+a[i]-2*t
        r+=max(abs(a[i]-t),abs(b[i]-t))
r+=abs(t-a[-1])
print r