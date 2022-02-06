from copy import copy


def get_best_score(rem):
    tmp_rem = copy(rem)
    if len(tmp_rem) == 0:
        return 0
    best = 0
    me = tmp_rem[0]
    for j in range(1, len(tmp_rem)):
        opo = tmp_rem[j]
        del tmp_rem[0]
        del tmp_rem[j-1]
        score = arr[me][opo-me-1] + get_best_score(tmp_rem)
        if score > best:
            best = score
    return best


n = int(input())
arr = []
for i in range(2 * n-1):
    li = list(map(int, input().split()))
    arr.append(li)

rem = list(range(2*n))

print(get_best_score(rem))
