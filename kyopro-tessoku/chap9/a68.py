import math


class Edge:
  def __init__(self, to, size, rev):
    self.to = to
    self.size = size
    self.rev = rev


class MSF:
  def __init__(self, n):
    self.n = n
    self.adjs = [[] for _ in range(n)]
    self.searched = [False] * n

  def add_edge(self, u, v, size):
    self.adjs[u].append(Edge(v, size, len(self.adjs[v])))
    self.adjs[v].append(Edge(u, 0, len(self.adjs[u]) - 1))

  def dfs(self, current, goal, F):
    self.searched[current] = True
    for edge in self.adjs[current]:
      if self.searched[edge.to]:
        continue
      if edge.size == 0:
        continue
      if edge.to == goal:
        flow = min(edge.size, F)
        self.__add_flow(edge, flow)
        return flow

      flow = self.dfs(edge.to, goal, min(edge.size, F))
      if flow > 0:
        self.__add_flow(edge, flow)
        return flow
    return 0

  def rest_flow(self, start, goal):
    self.searched = [False] * self.n
    return self.dfs(start, goal, math.inf)

  def max_flow(self, start, goal):
    result = 0
    while True:
      flow = self.rest_flow(start, goal)
      result += flow
      if flow == 0:
        break
    return result

  def __add_flow(self, edge: Edge, flow):
    edge.size -= flow
    self.adjs[edge.to][edge.rev].size += flow


n, m = list(map(int, input().split()))
msf = MSF(n)

for _ in range(m):
  a, b, c = list(map(int, input().split()))
  msf.add_edge(a - 1, b - 1, c)

print(msf.max_flow(0, n - 1))
