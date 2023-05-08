n, k = list(map(int, input().split()))

length = 2 * (n - 1)
ans = k >= length and (length - k) % 2 == 0

print('Yes' if ans else 'No')
