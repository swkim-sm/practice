import sys
Input = sys.stdin.readline
n, m = map(int, Input().split())
pos = list(map(int, Input().split()))
pos.sort()

last_points = []
for i in range(0, n, m):
    if pos[i] > 0:
        break
    last_points.append(-pos[i])

for i in range(n-1, -1, -m):
    if pos[i] < 0:
        break
    last_points.append(pos[i])

answer = sum(last_points)*2 - max(last_points)
print(answer)