import string

alphs = list(string.ascii_lowercase)
s = input()

ans = []
letters = {}

for letter in alphs:
    letters[letter] = 0

for letter in s:
    letters[letter] += 1

for letter in alphs:
    for i in range(letters[letter]):
        ans.append(letter)

print(''.join(ans))
