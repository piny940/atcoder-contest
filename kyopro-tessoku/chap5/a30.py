# p: 素数のときa**(p-1) % p = 1
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


n, r = list(map(int, input().split()))

ans = fact(n) * power(fact(r) * fact(n - r) % MOD, MOD - 2) % MOD

print(ans)
