# input
N = int(input())
tri = []
for i in range(N):
    tri.append(list(map(int, input().split())))

# perform
for n in range(N):
    if n != 0:
        for i, v in enumerate(tri[n]):
            if i == 0:
                tri[n][i] += tri[n-1][i]
            elif i == n:
                tri[n][i] += tri[n-1][i-1]
            else:
                tri[n][i] += max(tri[n-1][i-1], tri[n-1][i])

# output
answer = max(tri[-1])
print(answer)
