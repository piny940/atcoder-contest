n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

start = 1
end = 10 ** 9

def num(t):
  result = 0
  for i in range(n):
    result += t // arr[i]
  
  return result

# x以上を保ったまま探索する場合はendを含む配列で考える
while end - start > 0:
  middle = (start + end) // 2
  if num(middle) >= k:
    end = middle
  else:
    start = middle + 1

print(start)
