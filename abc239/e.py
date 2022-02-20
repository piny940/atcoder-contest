import heapq
import numpy as np


n, q = list(map(int, input().split()))
xrr = list(map(int, input().split()))

children = [[] for _ in range(n)]

