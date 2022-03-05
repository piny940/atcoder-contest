n = int(input())
m = 998244353

ans = 0

nums = [[0 for _ in range(9)] for _ in range(n)]

for i in reversed(range(n)):
    for j in range(9):
        if i == n-1:
            nums[i][j] = 1
        else:
            if j-1 >= 0:
                nums[i][j] += nums[i+1][j-1]
            if j+1 < 9:
                nums[i][j] += nums[i+1][j+1]
            nums[i][j] += nums[i+1][j]
        nums[i][j] %= m

for i in range(9):
    ans += nums[0][i]
    ans %= m

print(ans)
