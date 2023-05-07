from bisect import bisect_left as bisect

n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))

print(bisect(arr, x) + 1)
