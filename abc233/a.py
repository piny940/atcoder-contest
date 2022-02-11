x, y = list(map(int, input().split()))

ans = 0
while ans * 10 + x < y:
    ans += 1

print(ans)
