import sys
from collections import defaultdict
import heapq

# input
I = sys.stdin.readline

V, E = map(int, I().split())
start_point = int(I())
data = []
for i in range(E):
    data.append(list(map(int, I().split())))

graph = defaultdict(list)
for u, v, w in data:
    graph[u].append([v, w])

# perform
INF = 3000000
result = [INF for _ in range(V)]

heap = []
heapq.heappush(heap, (0, start_point))

result[start_point-1] = 0

while heap:
    cur_weight, cur_point = heapq.heappop(heap)

    if cur_weight > result[cur_point-1]:
        print(cur_weight, result[cur_point-1])
        continue

    for pos, wei in graph[cur_point]:
        tmp = cur_weight + wei
        if tmp < result[pos-1]:
            result[pos-1] = tmp
            heapq.heappush(heap, (tmp, pos))

# output
for r in result:
    if r == INF:
        print("INF")
    else:   
        print(r)
