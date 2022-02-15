from copy import copy


n, m = list(map(int, input().split()))

abrr = []
for i in range(m):
    abrr.append(set(map(int, input().split())))

cdrr = []
for i in range(m):
    cdrr.append(set(map(int, input().split())))

def is_able(prr):
    value = True
    for i in range(1, n+1):
        for j in range(1, n+1):
            in_abrr = {i, j} in abrr
            in_cdrr = {prr[i-1], prr[j-1]} in cdrr
            if in_abrr != in_cdrr:
                value = False
    return value

def explore(tmp_prr):
    if len(tmp_prr) == n:
        return is_able(tmp_prr)
    
    value = False
    for i in range(1, n+1):
        if i in tmp_prr:
            continue
        new_prr = copy(tmp_prr)
        new_prr.append(i)
        
        value = value | explore(new_prr)
    return value

prr = []

ans = explore(prr)

if ans:
    print('Yes')
else:
    print('No')
