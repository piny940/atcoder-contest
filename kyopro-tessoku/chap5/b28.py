n = int(input())
arr = [-1, 1, 1]

for i in range(3, n + 1):
  a = (arr[i - 1] + arr[i - 2]) % 1000000007
  arr.append(a)

print(arr[-1])
