n, m, b = list(map(int, input().split()))
arr = list(map(int, input().split()))
crr = list(map(int, input().split()))

asum = sum(arr)
csum = sum(crr)

print(asum * m + csum * n + n * m * b)
