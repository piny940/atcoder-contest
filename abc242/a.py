a, b, c, x = list(map(int, input().split()))


if x <= a:
    print(1)
elif a+1 <= x <= b:
    print(c / (b - a))
else:
    print(0)
