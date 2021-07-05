N = int(input())
costs = []
for i in range(N):
    cost = list(map(int, input().split()))
    costs.append(cost)


for i in range(1, N):
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])
    costs[i][1] += min(costs[i-1][0], costs[i-1][2])
    costs[i][2] += min(costs[i-1][0], costs[i-1][1])

answer = min(costs[N-1])
print(answer)
