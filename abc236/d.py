from copy import copy
import numpy as np


def get_best_score(rem):
    if len(rem) == 0:
        return 0
    best = 0
    me = rem[0]
    tmp_rem = np.delete(rem, 0)
    for j in range(len(tmp_rem)):
        opo = tmp_rem[j]
        tmp2 = np.delete(tmp_rem, j)
        score = arr[me][opo-me-1] + get_best_score(tmp2)
        if score > best:
            best = score
    return best


n = int(input())
arr = []
for i in range(2 * n-1):
    li = list(map(int, input().split()))
    arr.append(li)

rem = np.array(range(2*n))

print(get_best_score(rem))
