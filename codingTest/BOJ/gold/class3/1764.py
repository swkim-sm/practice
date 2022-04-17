import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g1 = set([input().rstrip() for _ in range(n)])
g2 = set([input().rstrip() for _ in range(m)])

ans = sorted(list(g1&g2))

print(len(ans))
for x in ans:
    print(x)

# heapq 로 해도 시간초과 났는데 집합으로 하니까 통과! 