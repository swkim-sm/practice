import sys
import heapq
input = sys.stdin.readline
INF = int(1e7)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start_point, end_point, cost = map(int, input().split())
    graph[start_point].append((end_point, cost))

def dijkstra(start):
    h = []
    distances = [INF] * (m+1)

    heapq.heappush(h, (0, start))
    distances[start] = 0

    while h:
        distance, cur_node = heapq.heappop(h)
        if distances[cur_node] < distance:
            continue

        for node, cost in graph[cur_node]:
            new_cost = distance + cost
            if new_cost < distances[node]:
                distances[node] = new_cost
                heapq.heappush(h, (new_cost, node))
    return distances

ans = 0
for i in range(1, n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    ans = max(ans, go[x]+back[i])
print(ans)