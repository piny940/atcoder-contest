a, b = list(map(int, input().split()))


def power(p, q):
  if q == 1:
    return p
  r = q % 2
  part = power(p, q // 2)
  return (part ** 2 * p ** r) % 1000000007


print(power(a, b))
