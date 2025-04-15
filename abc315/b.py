m = int(input())
days = list(map(int, input().split()))

target = (sum(days) + 1) // 2
current = 0
for i in range(m):
  day = days[i]
  if current + day >= target:
    print(f'{i+1} {target-current}')
    break
  current += day
