import sys
sys.setrecursionlimit(10**6)
Input = sys.stdin.readline

N = int(Input())
players = list(map(int, Input().split()))

# RULE
# 1. find the lowest ranker 
answer = 0
rank = sorted(players, reverse=True)

# 2. compare to both side of the lowest ranker
for cur in rank[:-1]:
    idx = players.index(cur)
    if idx == 0:
        answer += abs(players[idx+1]-cur)
    elif idx == len(players)-1:
        answer += abs(players[idx-1]-cur)
    else:
        answer += min(abs(players[idx+1]-cur), abs(players[idx-1]-cur))
    players.pop(idx)
print(answer)

# THINK : the reason finding the lowest not the highest 


# # time over or memory over code

# answer = 1000
# def do_play(player, result):
#     global answer
#     if len(player) == 1:
#         answer = min(result, answer)
#         return 
#     for i in range(len(player)-1):
#         tmp = result + abs(player[i]-player[i+1])
#         if tmp < answer:
#             np = player[:]
#             np.remove(max(player[i], player[i+1]))
#             do_play(np, tmp)

# do_play(players, 0)
# print(answer)