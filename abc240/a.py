a, b = list(map(int, input().split()))

ans = (b - a == 1 or b - a == 9)

if ans:
    print('Yes')
else:
    print('No')
