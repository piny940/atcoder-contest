n, X, Y = list(map(int, input().split()))
parr: list[int] = []
tarr: list[int] = []
for i in range(n - 1):
  p, t = list(map(int, input().split()))
  parr.append(p)
  tarr.append(t)
Q = int(input())
queries: list[int] = []
for _ in range(Q):
  q = int(input())
  queries.append(q)

# 出発時刻を3*5*7*8で割った余りごとの所要時間
D = 3 * 5 * 7 * 8
totals = []

for mod in range(D):
  t = X
  for i in range(n - 1):
    p = parr[i]
    # pの倍数の時刻になるまで待つ
    if (mod + t) % p != 0:
      t += p - ((mod + t) % p)
    t += tarr[i]
  t += Y
  totals.append(t)

for q in queries:
  print(q + totals[q % D])
