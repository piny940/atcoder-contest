l, r = list(map(int, input().split()))
s = input()

print(s[:l-1] + ''.join(reversed(list(s[l-1:r]))) + s[r:])
