n = int(input())
prr = list(map(int, input().split()))
maxp = max(prr[1:])
diff = maxp - prr[0]
ans = 0
if diff >= 0:
  ans = diff + 1

print(ans)
