n, k = list(map(int, input().split()))
s = input()
swts = list(s)
ans = (k - swts.count('1')) % 2 == 0

print('Yes' if ans else 'No')
