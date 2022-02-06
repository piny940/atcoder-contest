

s = int(998244353)

n_str = input()
digit = len(n_str) - 1
n = int(n_str)
sum = 0

digits = [int(10 ** i) % s for i in range(digit+1)]

def first():
    x = n % s
    ns = n // s
    sum = int((((s-1) * s // 2) % s * ns) % s + (x * (x + 1) // 2) % s)
    return sum

def mid():
    diff = n - 10 ** digit
    sum = int(0)
    for i in range(digit):
        sum += int(digits[i] * (10**(i+1)-10**i))
    sum += (digits[digit] * (diff+1)) % s
    return sum

print(int((first() - mid() + n) % s))
