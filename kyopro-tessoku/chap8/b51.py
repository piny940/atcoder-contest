s = input()

stack = []
ans = []
for i in range(len(s)):
  if s[i] == '(':
    stack.append(i)
  else:
    cor = stack.pop()
    ans.append((cor + 1, i + 1))

for pair in ans:
  print(*pair)
