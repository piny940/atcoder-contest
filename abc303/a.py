n = int(input())
s = input()
t = input()

ans = True

for i in range(n):
  if s[i] == t[i]:
    continue
  if {s[i], t[i]} == {'1', 'l'}:
    continue
  if {s[i], t[i]} == {'0', 'o'}:
    continue
  ans = False
  break

print('Yes' if ans else 'No')
