from collections import deque
import numpy as np


n, m = list(map(int, input().split()))

restricts = []
for i in range(m):
    a, b = tuple(map(int, input().split()))
    restricts.append((a-1, b-1))

adjacents = [[] for _ in range(n)]

for restrict in restricts:
    adjacents[restrict[0]].append(restrict[1])
    adjacents[restrict[1]].append(restrict[0])

ans = True

# There are only two adjacent people for each people
for i in range(n):
    if len(adjacents[i]) > 2:
        ans = False

if not ans:
    print('No')
    exit()

graphs = []
found = [False for _ in range(n)]

for i in range(n):
    if found[i] == True:
        continue
    found[i] = True
    graphs.append([i])
    to_search = deque([i])
    while to_search:
        j = to_search.popleft()
        ads = adjacents[j]
        for ad in ads:
            if not found[ad]:
                to_search.append(ad)
                found[ad] = True
                graphs[-1].append(ad)

for graph in graphs:
    ok = False
    for ver in graph:
        if len(adjacents[ver]) < 2:
            ok = True
    if not ok:
        ans = False
        break

if ans:
    print('Yes')
else:
    print('No')
