# しゃくとり法: 単調増加な配列の2要素の組み合わせのうち、差がk以下であるものの数を求める

n, k = list(map(int, input().split()))

arr = list(map(int, input().split()))

sums = [0] * n
prev = 0
for i in range(n):
  sums[i] = prev + arr[i]
  prev = sums[i]

ans = 0

idx = 0
for i in range(n):
  while idx < n and (sums[idx] if i == 0 else sums[idx] - sums[i-1]) <= k:
    idx += 1
  
  ans += idx - i

print(ans)  
