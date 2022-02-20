a, b, c, d = list(map(int, input().split()))


#引数nが素数かどうかを判定
def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1

is_takahashi = False

for n in range(a, b+1):
    n_ok = True
    for m in range(c, d+1):
        if is_prime(n+m):
            n_ok = False
    if n_ok:
        is_takahashi = True
        break

if is_takahashi:
    print('Takahashi')
else:
    print('Aoki')
