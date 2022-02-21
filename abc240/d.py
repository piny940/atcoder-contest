from collections import deque


n = int(input())

arr = list(map(int, input().split()))

log = deque([])
seqs = deque([])
ball_num = 0
numrr = []

for i in range(n):
    ball_num += 1
    if log and log[-1] == arr[i]:
        seqs[-1] += 1
        if seqs[-1] == arr[i]:
            ball_num -= arr[i]
            log.pop()
            seqs.pop()
    else:
        log.append(arr[i])
        seqs.append(1)
    numrr.append(ball_num)

for i in range(len(numrr)):
    print(numrr[i])
