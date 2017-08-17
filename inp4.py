n,m= map(int, raw_input().split())
ma = []
re = ''
for i in range(m):
    a,b = map(int, raw_input().split())
    ma+=[i for i in range(a-1,b)]
q =int(raw_input())

for i in range(q):
    c,d = map(int, raw_input().split())
    if (c not in ma) and (d not in ma):
        re += 'OK'+'\n'
        ma+=[i for i in range(c-1,d)]
    else:
        re+= 'NG'+'\n'
print re.strip()