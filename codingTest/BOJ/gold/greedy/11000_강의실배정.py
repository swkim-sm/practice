import sys
import heapq
input = sys.stdin.readline
n = int(input())
times = [list(map(int, input().split()))for _ in range(n)]
times.sort()

assigned = [times[0][1]]

for s, t in times[1:]:
    cmp_t = heapq.heappop(assigned) # 여기서 굳이 pop 했다 뒤에서 push 할 필요 없이 heapreplace 라는 함수도 있음
    if cmp_t > s:
        heapq.heappush(assigned, cmp_t)
    heapq.heappush(assigned, t)
print(len(assigned))