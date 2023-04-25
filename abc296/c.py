n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort(reverse=True)

for i in range(n):
  diff = arr[i] - x
  start = 0
  end = len(arr)
  while True:
    if end - start == 1 and arr[start] != diff:
      break
    
    middle = (start+end) // 2
    if arr[middle] < diff:
      end = middle
    else:
      start = middle

print('No')
