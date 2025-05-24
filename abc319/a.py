rates = '''tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481'''

scores = {}

for line in rates.splitlines():
  name, score_str = line.split(' ')
  scores[name] = int(score_str)

s = input()
print(scores[s])
