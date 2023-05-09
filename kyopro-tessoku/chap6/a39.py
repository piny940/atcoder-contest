n = int(input())
movies = []
TIME_LIMIT = 86400

for i in range(n):
  l, r = list(map(int, input().split()))
  movies.append([l, r])

movies = sorted(movies, key=lambda x: x[1])

current = 0
ans = 0
for movie in movies:
  if movie[0] >= current:
    current = movie[1]
    ans += 1

print(ans)
