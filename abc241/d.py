import bisect


arr = []

q = int(input())

for i in range(q):
    inputs = list(map(int, input().split()))
    if inputs[0] == 1:
        bisect.insort_left(arr, inputs[1])
    
    elif inputs[0] == 2:
        x, k = inputs[1], inputs[2]
        idx = bisect.bisect_right(arr, x) - 1
        if idx + 1 < k:
            print(-1)
        else:
            print(arr[idx - k + 1])
    
    elif inputs[0] == 3:
        x, k = inputs[1], inputs[2]
        idx = bisect.bisect_left(arr, x)
        if len(arr) - idx < k:
            print(-1)
        else:
            print(arr[idx + k - 1])
