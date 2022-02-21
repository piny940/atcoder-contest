import numpy as np


n, x = list(map(int, input().split()))

abrr = []
for i in range(n):
    abrr.append(list(map(int, input().split())))

crr = [abrr[i][1] - abrr[i][0] for i in range(n)]

crr = np.sort(crr)
asum = np.sum([abrr[i][0] for i in range(n)])
bsum = np.sum([abrr[i][1] for i in range(n)])

def explore(h, sum):
    if h == n - 1:
        return (sum == x or sum+crr[h] == x)
    if sum + crr[h] > x:
        return explore(h + 1, sum)
    
    return explore(h + 1, sum+crr[h]) or explore(h + 1, sum)

def explore2(h, sum):
    if h == n-1:
        return (sum == x or sum - crr[h] == x)
    
    if sum - crr[h] < x:
        return explore2(h + 1, sum)
    
    return explore2(h + 1, sum-crr[h]) or explore2(h + 1, sum)

ans = True
if bsum - x > x - asum:
    ans = explore(0, asum)
else:
    ans = explore2(0, bsum)

if ans:
    print('Yes')
else:
    print('No')
