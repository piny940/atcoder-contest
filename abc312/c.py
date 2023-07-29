import math

n, m = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
brr = sorted(list(map(int, input().split())))

brr2 = list(map(lambda x: x + 1, brr))
breakpoints = sorted(arr + brr2)

arr.append(math.inf)
brr.append(math.inf)

aindex = 0
bindex = 0

for i in range(len(breakpoints)):
  while arr[aindex] <= breakpoints[i]:
    aindex += 1
  while brr[bindex] < breakpoints[i]:
    bindex += 1
  if aindex >= m - bindex:
    print(breakpoints[i])
    exit()
