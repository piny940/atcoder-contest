n, m, d = list(map(int, input().split()))
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
arr.sort()
brr.sort()

max_value = -1
aidx = n - 1
bidx = m - 1
while aidx >= 0 and bidx >= 0:
  if arr[aidx] - brr[bidx] > d:
    aidx -= 1
  elif brr[bidx] - arr[aidx] > d:
    bidx -= 1
  else:
    max_value = arr[aidx] + brr[bidx]
    break

print(max_value)
