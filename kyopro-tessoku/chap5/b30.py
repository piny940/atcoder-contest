MOD = 1000000007


def power(p, q):
  if q == 1:
    return p % MOD
  r = q % 2
  part = power(p, q // 2)
  return (part**2 * p**r) % MOD


def fact(m):
  result = 1
  for i in range(1, m + 1):
    result *= i
    result %= MOD
  return result


def comb(n, r):
  return fact(n) * power(fact(r) * fact(n - r), MOD - 2) % MOD


# (h+w-2) C (w-1)

h, w = list(map(int, input().split()))

print(comb(h + w - 2, w - 1))
