import sys
import heapq
Input = sys.stdin.readline
n = int(Input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(Input()))

answer = 0
while True:
    if len(heap) == 1:
        break
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap, x+y)
    answer += (x+y)
print(answer)