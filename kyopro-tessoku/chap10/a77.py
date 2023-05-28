
n, l = list(map(int, input().split()))
k = int(input())
arr = [0] + list(map(int, input().split()))
MAX = l


def judge(m):
  length = 0
  num = 0
  last = 0
  for i in range(1, n + 1):
    diff = arr[i] - arr[i - 1]
    length += diff
    if length >= m and num < k:
      num += 1
      length = 0
      last = arr[i]

  return num >= k and l - last >= m


start = 0
end = MAX + 1

while end - start > 1:
  middle = (start + end) // 2
  if judge(middle):
    start = middle
  else:
    end = middle

print(start)
