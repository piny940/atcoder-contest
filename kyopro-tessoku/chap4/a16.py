n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
arr = [0] + arr
brr = [0, 0] + brr

drr = [0, arr[1]]

for i in range(2, n):
  drr.append(min(drr[i - 1] + arr[i], drr[i - 2] + brr[i]))

print(drr[n - 1])
