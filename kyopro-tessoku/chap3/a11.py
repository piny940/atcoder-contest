n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))

start = 0
end = len(arr)
while end - start > 1:
  middle = (start + end) // 2
  if x < arr[middle]:
    end = middle
  else:
    start = middle

print(start + 1)
