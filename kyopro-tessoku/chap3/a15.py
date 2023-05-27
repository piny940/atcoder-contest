from bisect import bisect_left as bisect

n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)

unique = []
unique.append(sorted_arr[0])
for i in range(1, len(sorted_arr)):
  if unique[-1] is not sorted_arr[i]:
    unique.append(sorted_arr[i])

brr = map(lambda x: bisect(unique, x) + 1, arr)

print(*brr)
