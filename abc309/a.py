a, b = list(map(int, input().split()))

ans = b - a == 1
if a == 3 or a == 6:
  ans = False

print('Yes' if ans else 'No')
