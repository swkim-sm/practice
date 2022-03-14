import sys
Input = sys.stdin.readline

N = int(Input())
times = [[0, 0] for _ in range(N)]
for i in range(N):
    n, start_time, end_time = map(int, Input().split())
    times[n-1] = [start_time, end_time]

answer = [0]
times.sort()
for i in range(N):
    if answer[0] <= times[i][0]:
        answer[0] = times[i][1]
    else:
        answer.append(times[i][1])
    answer.sort()
print(len(answer))