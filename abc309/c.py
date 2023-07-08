n, k = list(map(int, input().split()))
meds = []
for i in range(n):
  a, b = list(map(int, input().split()))
  meds.append((a, b))

max_day = max(map(lambda m: m[0], meds))

# diffにおけるindexと日付の対応{day: idx}
day_index_map = dict()

# 飲む薬の数が変化する日
change_days = []
for i in range(n):
  a = meds[i][0]
  day_index_map[a] = i
  change_days.append(a)

diffs = [0] * len(change_days)

for i in range(n):
  a, b = meds[i]
  diffs[i] -= b

change_days.sort()

prev = sum(map(lambda m: m[1], meds))

if prev <= k:
  print(1)
  exit()

for day in change_days:
  idx = day_index_map[day]
  prev += diffs[idx]
  if prev <= k:
    print(day + 1)
    exit()
