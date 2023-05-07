from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
q = int(input())

arr.sort()

for i in range(q):
  x = int(input())
  print(bisect_left(arr, x))
